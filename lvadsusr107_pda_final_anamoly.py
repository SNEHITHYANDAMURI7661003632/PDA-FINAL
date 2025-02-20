# -*- coding: utf-8 -*-
"""LVADSUSR107_PDA_FINAL_Anamoly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wyi8MAf9ZlVT525I_l_aB6ueTYq7oz-G
"""

import pandas as pd
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

df = pd.read_csv("/content/social_network.csv")
df.head()

df.isnull().sum()
df.fillna(df.mean(),inplace=True)

df.corr()
import seaborn as sns
sns.heatmap(df.corr(),annot=True)
df.duplicated().sum()
df.drop_duplicates()

sns.boxplot(df)

Q1 = df['social_connections'].quantile(0.25)
Q3 = df['social_connections'].quantile(0.75)
IQR = Q3 - Q1


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df[(df['social_connections'] >= lower_bound) & (df['social_connections'] <= upper_bound)]

print("Original DataFrame:")
print(df)
print("\nDataFrame after removing outliers:")
print(df_no_outliers)

from sklearn.ensemble import IsolationForest

features = ["login_activity", "posting_activity", "social_connections"]
X = df[features]

model = IsolationForest()
model.fit(X)
y_pred = model.predict(X)

df["anomaly_score"] = model.decision_function(X)
anomalies = df.loc[df["anomaly_score"] < 0]
df_test= pd.read_csv("/content/social_network.csv")
x=df_test[["login_activity", "posting_activity", "social_connections"]]
df_values=x.values

find=df_values

result=[]
for i in find:
  z=model.predict([i])
  if z==[1]:
    result.append('Not Anomaly')
  elif z==[-1]:
    result.append('Anomaly')
df_test['Anomaly']=result
print(df_test)

plt.scatter(df["social_connections"], df["anomaly_score"], label="Not Anomaly")
plt.scatter(anomalies["social_connections"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Social Connections")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()


df_test.head()