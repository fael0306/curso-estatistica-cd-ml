from scipy.stats import binom
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dadosbinomial = binom.rvs(size=1000, n=10, p=0.1)

print(dadosbinomial)
print(np.unique(dadosbinomial, return_counts=True))

sns.distplot(dadosbinomial, kde=False)
plt.show()