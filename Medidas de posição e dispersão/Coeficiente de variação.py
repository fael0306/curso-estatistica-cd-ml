import numpy as np
import math
import statistics as sts
from scipy import stats

dadosimpar = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155])
dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Cálculo manual do coeficiente de variação
def varianciadesviopadraovariacao(dataset):
    media = dataset.sum()/len(dataset)
    # Calculando desvios, variância e coeficiente de variação
    desvio = abs(dataset-media)
    desvio = desvio**2
    somadesvio = desvio.sum()
    v = somadesvio/len(dataset)
    cv = math.sqrt(v)/media*100
    return v, math.sqrt(v), cv

print(varianciadesviopadraovariacao(dadosimpar))
print(varianciadesviopadraovariacao(dados))