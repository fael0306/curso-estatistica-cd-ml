import numpy as np
from scipy.stats import t
from scipy import stats

dados = np.array([149., 160., 147., 189., 175., 168., 156., 160., 152.])

n = len(dados)
media = dados.mean()
desviopadrao = np.std(dados)

intervalos = t.interval(0.95, n-1, media, stats.sem(dados, ddof=0))
print(intervalos)

margemdeerro = media-intervalos[0]
print(margemdeerro)