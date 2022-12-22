import pandas as pd
import numpy as np
import statistics as sts

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\credit_data.csv")

# Verificando a quantidade de registros nulos na base de dados
print(dataset.isnull().sum())

# Verificando os nulos
nulos = dataset[dataset.isnull().any(axis=1)]
print(nulos)

# Substituindo os valores nulos pela média dos valores
dataset['age'] = dataset['age'].replace(to_replace=np.nan, value=dataset['age'].mean())

# Verificando novamente se há nulos na base de dados
print(dataset[dataset.isnull().any(axis=1)])

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Medidas de posição e dispersão\\autos.csv", encoding="ISO-8859-1")

print(dataset.head())

# Identificando valores faltantes
print(dataset.isnull().sum())
print(dataset['fuelType'].unique())

# Verificando valor da moda para substituir nos valores faltantes (usando a moda, pois são strings)
print(sts.mode(dataset['fuelType']))

# Substituindo os valores vazios pelo valor da moda
dataset['fuelType'] = dataset['fuelType'].replace(to_replace=np.nan, value = sts.mode(dataset['fuelType']))

print(dataset['fuelType'].unique())