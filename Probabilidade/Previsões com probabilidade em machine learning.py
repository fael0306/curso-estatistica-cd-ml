import pandas as pd
from sklearn.naive_bayes import GaussianNB
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Probabilidade\\credit_data.csv")
dataset.dropna(inplace=True)
print(dataset.head())

X = dataset.iloc[:,1:4].values
y = dataset.iloc[:,4].values

naivebayes = GaussianNB()
naivebayes.fit(X,y)

print(X[0],X[0].shape)
novo = X[0].reshape(1,-1)
print(novo.shape)

previsao = naivebayes.predict_proba(novo)
print(previsao)

print(np.argmax(previsao))