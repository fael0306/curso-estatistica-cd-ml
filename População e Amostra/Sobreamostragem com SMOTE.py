from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\credit_data.csv")

# Alocando as colunas 0, 1 e 2 em x
x = dataset.iloc[:, 1:4].values

# Alocando a primeira coluna
y = dataset.iloc[:, 4].values

smote = SMOTE(sampling_strategy='minority')
#x_over, y_over = smote.fit_resample(x, y)

#print(x_over.shape, y_over.shape)

#print(np.unique(y, return_counts=True))

#x_treinamento_o,x_teste_o,y_treinamento_o,y_teste_o = train_test_split(x_over,y_over,test_size=0.2,stratify=y_over)

#print(x_treinamento_o.shape,x_teste_o.shape)

#modelo_o = GaussianNB()
#modelo_o.fit(x_treinamento_o,y_treinamento_o)
#previsoes_o = modelo_o.predict(x_teste_o)
#print(accuracy_score(previsoes_o, y_teste_o))

#cm_o = confusion_matrix(previsoes_o, y_teste_o)
#print(cm_o)

#print(305/(305+19))
#print(324/(324+38))