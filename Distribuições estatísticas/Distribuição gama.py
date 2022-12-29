# Distribuição com valores assimétricos do lado direito

from scipy.stats import gamma
import matplotlib.pyplot as plt
import seaborn as sns

# Gerando 1000 números aleatórios baseados na Distribuição gama. Parâmetro a indica o ponto de decaimento.
dadosgama = gamma.rvs(a=4, size=1000)
print(dadosgama)

sns.distplot(dadosgama)
plt.show()

# Verificando mínimos e máximos
print(min(dadosgama), max(dadosgama))

