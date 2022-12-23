import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Distribuição normal (Gaussiana)
# Gerando números aleatórios em formato de Distribuição Normal
dadosnormal = stats.norm.rvs(size=1000)
# Para mostrar só o histograma: stats.norm.rvs(size=1000, kde = False)
# Para mostrar só a linha: stats.norm.rvs(size=1000, hist = False)
print(dadosnormal)

# Plotando o gráfico
sns.distplot(dadosnormal)
plt.show()

# Verificando algumas estatísticas
print(dadosnormal.mean(), np.median(dadosnormal), stats.mode(dadosnormal), np.var(dadosnormal), np.std(dadosnormal))

# Verificando que cerca de 50% está a 1 desvio padrão de distância da média
qtd1desvpdpos = np.sum(((dadosnormal>=np.std(dadosnormal)) & (dadosnormal<=np.std(dadosnormal)+1)))
qtd1desvpdneg = np.sum(((dadosnormal<=np.std(dadosnormal)) & (dadosnormal>=np.std(dadosnormal)-1)))
print(qtd1desvpdpos)
print(qtd1desvpdneg)
print((qtd1desvpdpos+qtd1desvpdneg)/len(dadosnormal)*100,"%")