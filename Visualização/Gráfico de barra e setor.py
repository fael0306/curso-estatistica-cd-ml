import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\census.csv")
dataset = pd.DataFrame(dataset)
#print(dataset.head())

#sns.barplot(x="sex", y="final-weight", data=dataset, hue="income")
#plt.show()

# Verificando somatório de educação de quem ganha mais ou menos do que 50 mil
dadosagrupados = dataset.groupby(["income"])["education-num"].sum()
#print(dadosagrupados)

# Gerando gráfico
#dadosagrupados.plot.bar()
#plt.show()

# Gerando gráfico
dadosagrupados.plot.pie()
plt.show()