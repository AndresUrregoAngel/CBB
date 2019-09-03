import boto3
from sagemaker.sklearn.estimator import SKLearn,SKLearnModel
from sagemaker import get_execution_role
import sagemaker
import json


def update_target(y_pred):
  if y_pred == 1:
    sport = "Athletics"
  elif y_pred == 2:
    sport = "Cricket"
  elif y_pred == 3:
    sport = "Football"
  elif y_pred == 4:
    sport = "Rugby"
  else:
    sport = "Tennis"
  
  return sport


def lambda_handler(event,context):
    
    
    input_text = event['body']
    
    endpoint_name = 'clf-scikit-endpoint'
    client = boto3.client('sagemaker-runtime')

    response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="text/csv",
        Body=input_text
        )
    
    result = response['Body']
    model_prediction = json.loads(result.read())
    
    sport = update_target(model_prediction['instances'][0]['features'])
       
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Model: Naive-Bayes , the prediction was {}'.format(sport))
    }