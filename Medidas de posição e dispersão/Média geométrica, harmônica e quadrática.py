from scipy.stats.mstats import gmean
from scipy.stats.mstats import hmean
import numpy as np
import math

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Média geométrica
print(gmean(dados))

# Média harmônica
print(hmean(dados))

# Média quadrática
def qmean(dados):
    return math.sqrt(sum(n*n for n in dados)/len(dados))
print(qmean(dados))

# Calculando desvio padrão das médias (para verificar que são bem parecidas) - extra
vet = [qmean(dados),gmean(dados),hmean(dados)]
desvpad = np.std(vet)
print(desvpad)
# Porcentagem de desvio
print("Desvio padrão das médias:",round(desvpad,2),"-",round(desvpad/np.mean(dados)*100,2),"%")