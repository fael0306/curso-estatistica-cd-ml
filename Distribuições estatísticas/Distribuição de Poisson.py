from scipy.stats import poisson
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dadospoisson = poisson.rvs(size=1000, mu=1)

print(min(dadospoisson), max(dadospoisson))
print(np.unique(dadospoisson, return_counts=True))

sns.distplot(dadospoisson, kde=False)
plt.show()