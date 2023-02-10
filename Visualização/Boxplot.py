import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\census.csv")
dataset = pd.DataFrame(dataset)

# O gráfico é interessante para visualizar quais dados fogem do padrão. O gráfico é dividido por quartis.
#sns.boxplot(dataset['age'])
#plt.show()

#sns.boxplot(dataset['education-num'])
#plt.show()

# Pegando alguns dados da tabela para gerar 
dataset2 = dataset.iloc[:, [0,4,12]]
#print(dataset2.head())

# Criando gráfico com mais de 1 atributo
sns.boxplot(data=dataset2)
plt.show()