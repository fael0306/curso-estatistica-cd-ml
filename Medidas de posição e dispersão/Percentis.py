import numpy as np
from scipy import stats

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

print(np.median(dados))

# Mediana
print(np.quantile(dados, 0.5))
print(np.percentile(dados,0.5))

# Elemento que está em 5%, 10% e 90% da base de dados. Valores personalizados, diferente dos quartis.
print(np.percentile(dados,5),np.percentile(dados,10),np.percentile(dados,90))
print(stats.scoreatpercentile(dados,5),stats.scoreatpercentile(dados,10),stats.scoreatpercentile(dados,90))

import pandas as pd

dataset = pd.DataFrame(dados)
print(dataset.head())
print(dataset.quantile([0.05,0.1,0.9]))