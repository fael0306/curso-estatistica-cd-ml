import math as mt
import pandas as pd
import random as rd
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\census.csv")

def amostragemporgrupos(dataset,ngrupos):
    # Gerando quantidade de pessoas por grupo
    tamgrupos = len(dataset)/ngrupos

    # Criando lista de grupos
    grupos = []
    idgrupo = 0
    cont = 0
    for k in dataset.iterrows():
        grupos.append(idgrupo)
        cont = cont+1
        if cont>tamgrupos:
            cont = 0
            idgrupo = idgrupo+1

    # Criando coluna de grupos e recebendo divisões criadas
    dataset['Grupo']=grupos

    # Selecionando um grupo aleatoriamente
    grupoescolhido = rd.randint(0,ngrupos)

    # Retornando o grupo escolhido
    return dataset[dataset['Grupo']==grupoescolhido]

# Gerando grupo a cada sqrt(len(dataset)) elementos
agrupamento = amostragemporgrupos(dataset, int(np.sqrt(len(dataset))))

# Imprimindo no formato: (Quantidade de elementos total, Quantidade de grupos) Grupo selecionado     Quantidade de elementos total
print(agrupamento.shape, agrupamento["Grupo"].value_counts())

# Visualizando agrupamento selecionado
print(agrupamento)

# Média de idade de todas as pessoas da base
print(dataset['age'].mean().__round__(2))

# Média de idade das pessoas retiradas da amostra
print(agrupamento['age'].mean().__round__(2))