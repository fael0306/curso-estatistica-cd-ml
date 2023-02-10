import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Correlação e regressão\\house_prices.csv")
print(dataset.head())

dataset.drop(labels=['id', 'date'], axis = 1, inplace = True)
print(dataset.head())

#fig, ax  = plt.subplots(figsize=(15,15))
#sns.heatmap(dataset.corr(), annot=True)
#plt.show()
# No gráfico, é possível verificar que o melhor previsor de preços é o metro quadrado
# Pois a correlação é grande entre eles

# Coeficiente de correlação - % do preço da casa que pode ser explicado pelo metro quadrado
print(math.pow(0.7, 2))

# Regressão linear simples
X = dataset['sqft_living'].values
print(X.shape)
X = X.reshape(-1,1)
print(X.shape)
y = dataset['price'].values

# Fazendo o treinamento
from sklearn.model_selection import train_test_split
Xtreinamento, Xteste, ytreinamento, yteste = train_test_split(X,y,test_size=0.2,random_state=1)
print(Xtreinamento, Xteste)
# Criando a regressão
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(Xtreinamento, ytreinamento)

# Sendo y = ax+b
# Achando b
b = regressor.intercept_
# Achando a
a = regressor.coef_

# Verificando previsão de preço para metragem quadrada de 770 (na tabela seria 180000)
print(a*770+b)
# Previsão indica 180656, um preço parecido

# Fazendo o mesmo usando predict para uma metragem de 900
print(regressor.predict(np.array([[900]])))

plt.scatter(X,y)
plt.plot(X, regressor.predict(X), color='red')
#plt.show()

# Quanto mais próximo de 1, melhor o modelo
print(regressor.score(Xtreinamento, ytreinamento))
print(regressor.score(Xteste, yteste))