import numpy as np
import statistics
from scipy import stats
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Média aritmética
print(dados.sum()/len(dados))
print(dados.mean())
print(statistics.mean(dados))

# Moda
print(statistics.mode(dados))
print(stats.mode(dados))


dadosimpar = [150,151,152,152,153,154,155,155,155]

# Mediana com número ímpar de elementos: cálculo manual
posicao = len(dadosimpar)/2
print(posicao)
# Achando a posição da mediana
posicao = math.ceil(posicao)
print(posicao)
print(dadosimpar[posicao-1])

# Mediana com número par de elementos: cálculo manual
posicao = len(dados)//2
print(posicao)
# Achando os dados do meio
print(dados[posicao-1], dados[posicao])
# Calculando
mediana = (dados[posicao-1]+dados[posicao])/2
print(mediana)

# Calculando com as bibliotecas
print(np.median(dadosimpar))
print(np.median(dados))
print(statistics.median(dadosimpar))
print(statistics.median(dados))