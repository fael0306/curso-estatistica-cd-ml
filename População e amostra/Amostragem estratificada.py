from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\census.csv")

# Verificando quantidade de pessoas por salário anual
print(dataset['income'].value_counts())

# Mostrando porcentagem de pessoas que ganha mais e menos de 50 mil por ano
print(7841/len(dataset)) # +
print(24720/len(dataset)) # -

def amostragemestratificada(dataset,percentual):
    # Indicando tamanho da amostra
    split = StratifiedShuffleSplit(test_size=percentual, random_state=1)

    # Separando os dados da amostra aleatoriamente na variável df_y
    for _,y in split.split(dataset, dataset['income']):
        df_y = dataset.iloc[y]
    return df_y

df_amostragemestratificada = amostragemestratificada(dataset, 0.01)

# Verificando a quantidade de registros na amostra separada (df_y)
print(df_amostragemestratificada.shape)

# Verificando os registros que foram separados para a amostra
print(df_amostragemestratificada.head())

# Verificando que a amostra é estratificada
print(df_amostragemestratificada['income'].value_counts())

# Média de idade de todas as pessoas da base
print(dataset['age'].mean().__round__(2))

# Média de idade das pessoas retiradas da amostra
print(df_amostragemestratificada['age'].mean())