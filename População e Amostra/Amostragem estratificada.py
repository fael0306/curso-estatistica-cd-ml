from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd 

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\census.csv")

# Verificando quantidade de pessoas por salário anual
print(dataset['income'].value_counts())

# Mostrando porcentagem de pessoas que ganha mais e menos de 50 mil por ano
print(7841/len(dataset)) # +
print(24720/len(dataset)) # -

# Indicando tamanho da amostra (1% dos registros)
split = StratifiedShuffleSplit(test_size=0.01)

# Separando os dados da amostra aleatoriamente na variável df_y
for x,y in split.split(dataset, dataset['income']):
    df_x = dataset.iloc[x]
    df_y = dataset.iloc[y]

# Verificando a quantidade de registros na amostra separada (df_y)
print(df_x.shape, df_y.shape)

# Verificando os registros que foram separados para a amostra
print(df_y.head())

# Verificando que a amostra é estratificada
print(df_y['income'].value_counts())