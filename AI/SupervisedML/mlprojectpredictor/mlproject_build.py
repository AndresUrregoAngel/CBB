import argparse
import pandas as pd
import numpy as np
import json
import os
import pickle
import boto3
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sagemaker_containers.beta.framework import (
    content_types, encoders, env, modules, transformer, worker)


def getvectorizer():
    """
    Call vectorizer store in s3
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vectkey = "vectorizer.pickle"
    vectorizerpath = dir_path+"/"+vectkey
    client = boto3.client("s3")
    response = client.download_file("bucket",vectkey,vectorizerpath)
        
    print("The file has been download successfully at local path")
    
    vfile = open(vectorizerpath,"rb")  
    vectorizer = pickle.load(vfile)
    vfile.close()
    
    return vectorizer


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    # Hyperparameters are described here. In this simple example we are just including one hyperparameter.
    # parser.add_argument('--max_leaf_nodes', type=int, default=-1)

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    raw_data = [ pd.read_csv(file, sep=",", engine="python") for file in input_files ]
    fulldata = pd.concat(raw_data)

    # labels are in the first column
    X = fulldata.drop(['target'],axis=1)
    y = fulldata['target']
      
    # Preprocessing scaler
      
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
      
      
    # Split datasets
    n_splits=15
    cv = KFold(n_splits=n_splits,shuffle=True,random_state=1)
      
    for train_index,test_index in cv.split(X):
        X_train, X_test, y_train, y_test = X[train_index],X[test_index], \
                                           y[train_index],y[test_index]

    # Here we support a single hyperparameter, 'max_leaf_nodes'. Note that you can add as many
    # as your training my require in the ArgumentParser above.
    # max_leaf_nodes = args.max_leaf_nodes
    print(X_train.shape)
    # Now use scikit-learn's decision tree classifier to train the model.
    clf = GaussianNB()
    clf = clf.fit(X_train, y_train)

    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))
    

    
def input_fn(input_data, content_type):
    """Parse input data payload

    We currently only take csv input. Since we need to process both labelled
    and unlabelled data we first determine whether the label column is present
    by looking at how many columns were provided.
    """
#     if content_type == 'text/csv':
        
#         # Read the raw input data as CSV.
#         ifile = open(input_data,"rb")
#         content = ifile.read()
#         ifile.close()
        
#         dfile = pd.DataFrame(content,columns=['words'])
        
    lfile = []
    lfile.append(input_data)
    data = {"words":lfile}
    dfile = pd.DataFrame.from_dict(data)
    vectorizer = getvectorizer()
    X = vectorizer.transform(dfile['words'])
        
#     columns = ["var{}".format(i) for i in range(X.toarray().shape[1])]
#     df = pd.DataFrame(X.toarray(),columns=columns) 
    input_data =  X.toarray()

    return input_data
#     else:
#         raise ValueError("{} not supported by script!".format(content_type))

        
def predict_fn(input_data, model):
    """Preprocess input data

    We implement this because the default predict_fn uses .predict(), but our model is a preprocessor
    so we want to use .transform().

    The output is returned in the following order:

        rest of features either one hot encoded or standardized
    """
    prediction = model.predict(input_data)
    pred_prob = model.predict_proba(input_data)
    
    return prediction
    
def output_fn(prediction, accept):
    """Format prediction output

    The default accept/content-type between containers for serial inference is JSON.
    We also want to set the ContentType or mimetype as the same value as accept so the next
    container can read the response payload correctly.
    """
    if accept == "application/json":
        instances = []
        for row in prediction.tolist():
            instances.append({"features": row})

        json_output = {"instances": instances}

        return worker.Response(json.dumps(json_output), accept, mimetype=accept)
    elif accept == 'text/csv':
        return worker.Response(encoders.encode(prediction, accept), accept, mimetype=accept)
    else:
        raise Exception("{} accept type is not supported by this script.".format(accept))
    
    
    
def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

