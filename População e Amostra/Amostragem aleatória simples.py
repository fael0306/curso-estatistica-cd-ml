import pandas as pd
import random
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\covid.csv")

# Linhas e colunas
print(dataset.shape)
# Mostra as 5 primeiras linhas e colunas
print(dataset.head())
# Mostra os últimos registros da base
print(dataset.tail())

# Selecionando amostra aleatória
amostra = dataset.sample(n=7, replace=False, random_state=1)
print(amostra)
