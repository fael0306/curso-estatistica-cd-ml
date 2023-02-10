import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Correlação e regressão\\house_prices.csv")
print(dataset.head())

dataset.drop(labels=['id', 'date'], axis = 1, inplace = True)
print(dataset.head())

fig, ax  = plt.subplots(figsize=(15,15))
sns.heatmap(dataset.corr(), annot=True)
plt.show()

# Serão utilizadas as maiores 4 correlações com o preço
X = dataset.iloc[:, [2,3,9,10]].values
#print(X)
y = dataset.iloc[:, 0].values

# Fazendo o treinamento
from sklearn.model_selection import train_test_split
Xtreinamento, Xteste, ytreinamento, yteste = train_test_split(X,y,test_size=0.2,random_state=1)
print(Xtreinamento.shape, Xteste.shape)

# Criando a regressão linear
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(Xtreinamento, ytreinamento)
print(regressor.score(Xtreinamento, ytreinamento))
print(regressor.score(Xteste, yteste))
# Verificando erro absoluto da previsão
from sklearn.metrics import mean_absolute_error
previsoes = regressor.predict(Xteste)
print(mean_absolute_error(yteste, previsoes))

import matplotlib.pyplot as plt
#f, ax = plt.subplots(2, 2)
#ax[0,0].hist(X[0])
#ax[0,1].hist(X[1])
#ax[1,0].hist(X[2])
#ax[1,1].hist(X[3])
#plt.show()

#plt.hist(y)
#plt.show()

# Transformando em distribuição normal
y = np.log(y)
#plt.hist(y)
#plt.show()

# Refazendo teste
from sklearn.model_selection import train_test_split
Xtreinamento, Xteste, ytreinamento, yteste = train_test_split(X,y,test_size=0.2,random_state=1)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(Xtreinamento, ytreinamento)
# Verificando melhoria
print(regressor.score(Xtreinamento, ytreinamento))
print(regressor.score(Xteste, yteste))