import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\census.csv")
dataset = pd.DataFrame(dataset)
#print(dataset.head())

# O atributo hue faz agrupamento pelo atributo selecionado
# Style muda o tipo de marcação no gráfico de acordo com o atributo selecionado
# Size faz aumentar o tamanho da marcação de acordo com o atributo escolhido
sns.relplot(x="age", y="final-weight", data=dataset, hue="sex", style="income", size="education-num")
plt.show()
# É possível verificar que não há relação entre os atributos age e final-weight