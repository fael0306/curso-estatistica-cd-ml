import numpy as np
import statistics as sts
from scipy import ndimage

dadosimpar = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155])
dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Cálculo manual
def variancia(dataset):
    media = dataset.sum()/len(dataset)
    # Calculando desvios e variância
    desvio = abs(dataset-media)
    desvio = desvio**2
    somadesvio = desvio.sum()
    v = somadesvio/len(dataset)
    return v

print(variancia(dadosimpar))
print(variancia(dados))

# Usando numpy
print(np.var(dadosimpar))
print(np.var(dados))

# Usando statistics
print(sts.variance(dadosimpar))
print(sts.variance(dados))

# Usando scipy
print(ndimage.variance(dadosimpar))
print(ndimage.variance(dados))