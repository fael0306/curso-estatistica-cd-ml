import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Distribuições estatísticas\\house_prices.csv")

print(dataset.head())

#sns.distplot(dataset["price"])
#plt.show()
#sns.distplot(dataset["sqft_living"])
#plt.show()

# O x da função será o metro quadrado e o y será o preço. 
# Será feita uma regressão linear para observar a variação do preço de acordo com o metro quadrado

# Sem tratamento de dados #
X = dataset['sqft_living'].values
print(X)
print(X.shape)
# Transformando dados em matriz para usar o algoritmo do sklearn
X = X.reshape(-1,1)
print(X.shape)
y = dataset['price'].values
print(y)
# Criando o modelo da regressão
regressor = LinearRegression()
regressor.fit(X,y)
# Criando as previsões
previsoes = regressor.predict(X)
# Verificando a acurácia das previsões (retorna a média de erro absoluto no cálculo das previsões)
print(mean_absolute_error(y, previsoes))
# Verificando a acurácia das previsões (retorna um coeficiente que dita se o resultado é bom)
# Quanto mais próximo de 1, melhor
print(r2_score(y, previsoes))

# Com tratamento de dados #
# Criando uma função logarítimica 
Xnovo = np.log(X)
print(Xnovo)
#sns.distplot(Xnovo)
#plt.show()
# Gerando outra regressão linear
ynovo = np.log(y)
print(ynovo)
sns.distplot(ynovo)
plt.show()
print(mean_absolute_error(ynovo, previsoes))
print(r2_score(ynovo, previsoes))
regressor = LinearRegression()
regressor.fit(Xnovo,y)
previsoes = regressor.predict(Xnovo)
print(mean_absolute_error(y, previsoes))
print(r2_score(y, previsoes))