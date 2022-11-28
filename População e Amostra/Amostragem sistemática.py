import math as mt
import pandas as pd
import random as rd
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\covid.csv")

def amostragemsistematica(dados, amostras):

    # Pegando tamanho de intervalo para amostra dos dados
    intervalo = int(len(dados)/amostras)

    rd.seed(1)

    # Pegando número de onde partirá a amostra
    inicio = rd.randint(0,intervalo)

    # Pegando números aleatórios para a amostra a partir do número onde a amostra começa
    indices = np.arange(inicio,len(dados),step=intervalo)

    # Criando amostras a partir dos índices selecionados
    amostra = dados.iloc[indices]

    return amostra

print(amostragemsistematica(dataset,100))