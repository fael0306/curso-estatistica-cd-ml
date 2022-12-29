from scipy.stats import uniform
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dadosuniforme = uniform.rvs(size=1000)

#sns.distplot(dadosuniforme)
#plt.show()

print(min(dadosuniforme),max(dadosuniforme))
# Verificando que a quantidade é igual para todos os elementos
print(np.unique(dadosuniforme, return_counts=True))

# Gerando gráfico com 30 intervalos de classes para verificar que continua uniforme
sns.distplot(dadosuniforme, bins=30)
plt.show()