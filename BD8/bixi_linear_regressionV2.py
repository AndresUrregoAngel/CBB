# _*_ coding: UTF-8 _*_

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.utils import column_or_1d
from sklearn import metrics
import numpy as np


df = pd.read_csv('bixi_final.csv',dtype={"user_id": int},low_memory= False,sep=',',encoding = "ISO-8859-1")
df_clNA = df.fillna(0)

#print(df.dtypes)
#print(test.where(df.id == 274680).dropna(thresh=2).head(n=20))

month = df_clNA.mois
month_encoder = preprocessing.LabelEncoder()
month_encoder.fit(month)
mois_formatted = month_encoder.transform(df_clNA['mois'])

jour = df_clNA.jour
jour_encoder = preprocessing.LabelEncoder()
jour_encoder.fit(jour)
jour_formatted = jour_encoder.transform(df_clNA['jour'])


action = df_clNA.action.astype(str)
action_encoder = preprocessing.LabelEncoder()
action_encoder.fit(action)
action_formatted = action_encoder.transform(df_clNA['action'].astype(str))


df_normalized = df_clNA.drop(['mois','jour','action'], axis=1)
df_normalized['mois'] = mois_formatted
df_normalized['jour'] = jour_formatted
df_normalized['action'] = action_formatted


#print(df_normalized.shape)
#print(df_normalized.head())
#print(df_normalized.describe())


y = df_normalized.action
X = df_normalized.drop(['action','id'],axis=1).astype('float64')




print(X.head())

# split training and test
X_train, X_test,y_train,y_test = train_test_split (X,y,test_size=0.25,random_state = 33)

# Apply the scaler
scalerX = StandardScaler().fit(X_train)
scalery = StandardScaler().fit(y_train.reshape(-1,1))
X_train = scalerX.transform(X_train)
y_train = scalery.transform(y_train.reshape(-1,1))

# split the tragets in training/test
X_test = scalerX.transform(X_test)
y_test = scalery.transform(y_test.reshape(-1,1))

# Create model linear regression
clf_sgd = linear_model.SGDRegressor(loss='squared_loss',penalty=None,random_state=42)

# Learning based in the model
clf_sgd.fit(X_train,y_train.ravel())

print("Coefficient de determination:",clf_sgd.score(X_train,y_train))
# Model performance
y_pred = clf_sgd.predict(X_test)
print("Coefficient de determination:{0:.3f}".format(metrics.r2_score(y_test,y_pred)))
