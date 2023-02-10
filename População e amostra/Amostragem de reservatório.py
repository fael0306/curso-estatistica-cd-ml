import pandas as pd
import random

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\census.csv")

def amostragem_reservatorio(dataset, amostras):
    stream = []
    # Criando lista com os índices do dados do dataset
    for k in range(len(dataset)):
        stream.append(k)
    i = 0
    tamanho = len(dataset)
    # Criando lista de reservatório com o tamanho escolhido para a quantidade de amostras que o reservatório terá
    reservatorio = [0]*amostras
    # Inicializando o reservatório de acordo com os elementos do dataset
    for i in range(amostras):
        reservatorio[i] = stream[i]

    while i<tamanho:
        # Sorteando um índice que esteja dentro do tamannho do dataset
        j = random.randrange(i+1)
        # Dentro de reservatório estarão todos os números sorteados
        if j<amostras:
            reservatorio[j]=stream[i]
        i=i+1

        return dataset.iloc[reservatorio]

df_amostragem_reservatorio = amostragem_reservatorio(dataset,100)

# Verificando se está retornando número correto de registros
print(df_amostragem_reservatorio.shape)

# Mostrando primeiros registros selecionados na amostragem obtida
print(df_amostragem_reservatorio.head())

# Média de idade de todas as pessoas da base
print(dataset['age'].mean().__round__(2))

# Média de idade das pessoas retiradas da amostra
print(df_amostragem_reservatorio['age'].mean().__round__(2))