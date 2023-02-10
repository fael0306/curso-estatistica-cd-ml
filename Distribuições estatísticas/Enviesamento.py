from scipy.stats import skewnorm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Gerando dados em formato normal sem enviesamento (a=0)
dadosnormal = skewnorm.rvs(a=0, size=1000)
# PLOTANDO GRÁFICO
#sns.distplot(dadosnormal)
#plt.show()

# Verificando estatísticas
print(dadosnormal.mean(), np.median(dadosnormal), stats.mode(dadosnormal))

# Gerando dados com enviesamento positivo (a=10)
dadosnormal = skewnorm.rvs(a=10, size=1000)
# PLOTANDO GRÁFICO
#sns.distplot(dadosnormal)
#plt.show()

# Verificando estatísticas
print(dadosnormal.mean(), np.median(dadosnormal), stats.mode(dadosnormal))

# Gerando dados com enviesamento negativo (a=-10)
dadosnormal = skewnorm.rvs(a=-10, size=1000)
# PLOTANDO GRÁFICO
#sns.distplot(dadosnormal)
#plt.show()

# Verificando estatísticas
print(dadosnormal.mean(), np.median(dadosnormal), stats.mode(dadosnormal))