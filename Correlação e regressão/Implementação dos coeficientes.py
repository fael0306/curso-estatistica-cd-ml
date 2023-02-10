import numpy as np
import pandas as pd
import seaborn as sns
import math
import matplotlib.pyplot as plt

tamanho = np.array([30,39,49,60])
preco = np.array([57000,69000,77000,90000])

dataset = pd.DataFrame({'Tamanho': tamanho, 'Preço': preco})
#print(dataset)

mediatamanho = dataset['Tamanho'].mean()
mediapreco = dataset['Preço'].mean()
#print(mediatamanho, mediapreco)

dptamanho = dataset['Tamanho'].std()
dppreco = dataset['Preço'].std()
#print(dptamanho, dppreco)

# Cálculo manual da correlação
dataset['Dif'] = (dataset['Tamanho']-mediatamanho)*(dataset['Preço']-mediapreco)
somadif = dataset['Dif'].sum()
covariancia = somadif/(len(dataset)-1) # Calculando a covariância pela fórmula
coefcorrelacao = covariancia/(dptamanho*dppreco)
print(coefcorrelacao)

# Verificando a correlação linear
#sns.scatterplot(x=tamanho,y=preco)
#plt.show()

coeficientedeterminacao = math.pow(coefcorrelacao, 2)
print(coeficientedeterminacao)

# Covariância
# Usando Numpy
print(np.cov(tamanho, preco))
# Usando Pandas
print(dataset.cov())

# Coeficiente de correlação - melhoria na visualização em relação à covariância
# Usando Numpy
print(np.corrcoef(tamanho, preco))
# Usando Pandas
print(dataset.corr())