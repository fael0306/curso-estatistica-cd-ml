import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

# Criando dicionário para gerar números aleatórios
baseselecao = {'a': np.random.rand(20),
               'b': np.array([0.5]*20),
               'classe': np.random.randint(0, 2, size = 20)}

#print(baseselecao)

# Criando tabela com os valores gerados
dataset = pd.DataFrame(baseselecao)
print(dataset.head())

# Verificando estatísticas da tabela
print(dataset.describe())

# Verificando variância de cada atributo
print(np.var(dataset['a']),np.var(dataset['b']))

X = dataset.iloc[:, 0:2].values
print(X)

# Excluindo valores que possuem variância menor do que a desejada
selecao = VarianceThreshold(threshold=0.07)
Xnovo = selecao.fit_transform(X)
print(Xnovo, Xnovo.shape)

# Verificando variâncias
print(selecao.variances_)

# Verificando quais valores possuem a variância menor do que a desejada (os que foram excluídos) - nesse caso só existe 1
indices = np.where(selecao.variances_>0.07)
print(indices)