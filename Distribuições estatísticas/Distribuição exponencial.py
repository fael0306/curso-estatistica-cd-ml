from scipy.stats import expon
import matplotlib.pyplot as plt
import seaborn as sns

# Gerando dados em distribuição exponencial
dadosexponencial = expon.rvs(size=1000)

sns.distplot(dadosexponencial)
plt.show()

print(min(dadosexponencial),max(dadosexponencial))