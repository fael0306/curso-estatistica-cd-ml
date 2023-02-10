import numpy as np
import math
import statistics as sts
from scipy import stats

dadosimpar = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155])
dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Cálculo manual da variância
def varianciadesviopadrao(dataset):
    media = dataset.sum()/len(dataset)
    # Calculando desvios e variância
    desvio = abs(dataset-media)
    desvio = desvio**2
    somadesvio = desvio.sum()
    v = somadesvio/len(dataset)
    return v, math.sqrt(v)

print(varianciadesviopadrao(dadosimpar))
print(varianciadesviopadrao(dados))

# Com Numpy
print(np.std(dadosimpar))
print(np.std(dados))

# Com Statistics
print(sts.stdev(dadosimpar))
print(sts.stdev(dados))

# Com Scipy
print(stats.tstd(dados, ddof=0))