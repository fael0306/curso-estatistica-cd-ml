import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Intervalos de confiança e testes de hipóteses\\trip_d1_d2.csv', sep=';')

#print(dataset.head())

#sns.distplot(dataset['D1'])
#plt.show()

#sns.distplot(dataset['D2'])
#plt.show()

# Testes de Shapiro para saber se as distribuições são normais
# Alpha = 0,05
from scipy.stats import shapiro

print(shapiro(dataset['D1']), shapiro(dataset['D2']))
# Não é distribuição normal, pois pvalue<0,05
# Dessa forma, é necessário aplicar o teste de Friedman

#from scipy.stats import friedmanchisquare

#_,p = friedmanchisquare(dataset['D1'], dataset['D2'])
# Teste de Friedman não serve pois só pode ser feito com 3 bases ou mais
# Dessa forma, será feito o teste de Wilcoxon

from scipy.stats import wilcoxon

_,p = wilcoxon(dataset['D1'], dataset['D2'])
print(p)

# Mostrando que os dados são diferentes através da média
print(dataset['D1'].mean(), dataset['D2'].mean())