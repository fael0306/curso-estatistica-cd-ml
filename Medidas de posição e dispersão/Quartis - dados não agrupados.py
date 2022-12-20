import numpy as np
import math
from scipy import stats

dadosimpar = [150, 151, 152, 152, 153, 154, 155, 155, 155]

mediana = np.median(dadosimpar)
print(mediana)

posicaomediana = math.floor(len(dadosimpar)/2)
print(posicaomediana)

# Criando primeiro quartil (do elemento 0 até o 3. O posicaomediana não entra.)
esquerda = dadosimpar[0:posicaomediana]
# Encontrando mediana do primeiro quartil para encontrar próximo quartil
mediana1quartil = np.median(esquerda)

# Criando terceiro quartil (do elemento posicaomediana até o último)
direita = dadosimpar[posicaomediana+1:]
mediana3quartil = np.median(direita)

# Quartis
print(esquerda, direita)

# Usando numpy para encontrar a mediana
print(np.quantile(dadosimpar, 0.5))

# Usando numpy para encontrar o terceiro quartil
print(np.quantile(dadosimpar, 0.75))

# Usando numpy para encontrar o primeiro quartil
print(np.quantile(dadosimpar, 0.25))

# Considerando a mediana
esquerda2 = dadosimpar[0:posicaomediana+1]
print(esquerda2)
print(np.median(esquerda2))

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Verificando quartis da base de dados completa
print(np.quantile(dados,0.25), np.quantile(dados,0.50), np.quantile(dados,0.75))

# Usando scipy
print(stats.scoreatpercentile(dados,25),stats.scoreatpercentile(dados,50),stats.scoreatpercentile(dados,75))

import pandas as pd

# Criando dataset em pandas para verificar quartis
dataset = pd.DataFrame(dados)
print(dataset.head())

# Verificando quartis com pandas
print(dataset.quantile([0.25, 0.5, 0.75]))
# Gerando algumas estatísticas da base de dados
print(dataset.describe())