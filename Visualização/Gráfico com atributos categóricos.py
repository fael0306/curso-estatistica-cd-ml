import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\census.csv")

# Criando gráfico para visualizar salário em relação às horas trabalhadas, separando por sexo
#sns.catplot(x="income", y="hour-per-week", data=dataset, hue="sex")
#plt.show()

# Filtrando para aparecer somente idades >50
#sns.catplot(x="income", y="hour-per-week", hue="sex", data=dataset.query("age>50"))
#plt.show()

# Filtrando para aparecer somente idades <30
sns.catplot(x="income", y="hour-per-week", hue="sex", data=dataset.query("age<30"))
plt.show()