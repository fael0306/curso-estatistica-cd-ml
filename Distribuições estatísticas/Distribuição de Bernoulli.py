from scipy.stats import bernoulli
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dados com 50% de probabilidade
dadosbernoulli = bernoulli.rvs(size=1000, p = 0.5)

print(np.unique(dadosbernoulli, return_counts=True))

sns.distplot(dadosbernoulli, kde=False)
plt.show()

