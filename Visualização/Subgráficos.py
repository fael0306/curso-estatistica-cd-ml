import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\census.csv")

# Separando por sexo
g = sns.FacetGrid(dataset, col="sex", hue="income")
g.map(sns.scatterplot, "age", "final-weight")
plt.show()

# Separando por tipo de trabalho
g = sns.FacetGrid(dataset, col="workclass", hue="income")
g.map(sns.scatterplot, "age", "final-weight")
plt.show()

g = sns.FacetGrid(dataset, col="sex", hue="income")
g.map(sns.histplot, "age")
plt.show()

dataset2 = dataset.iloc[:, [0,4,12]]
g = sns.PairGrid(dataset2)
g.map(sns.scatterplot)
plt.show()

g = sns.PairGrid(dataset2)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
plt.show()