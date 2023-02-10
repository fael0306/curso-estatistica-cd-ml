# Prevendo se a postagem é um anúncio baseado em informações sobre a postagem

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectFdr
from sklearn.feature_selection import f_classif
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('C:\\Users\\f0fp1107\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Intervalos de confiança e testes de hipóteses\\ad.data', header=None)
print(dataset.head())

X = dataset.iloc[:, 0:1558].values
y = dataset.iloc[:, 1558].values

print(np.unique(y, return_counts=True))

# Prevendo e verificando porcentagem de acerto da previsão
naive1 = GaussianNB()
naive1.fit(X,y)
previsoes1 = naive1.predict(X)
print(accuracy_score(y, previsoes1))

selecao = SelectFdr(f_classif, alpha=0.01)
# Colocando em outra variáveis as melhores características selecionadas
X_novo = selecao.fit_transform(X,y)

print(X.shape,X_novo.shape)

# Verificando os atributos que possuem p<=0.01
print(np.sum(selecao.pvalues_<=0.01))

# Retorna quais colunas foram selecionadas a partir do p
colunas = selecao.get_support()

# Verificando quais colunas foram selecionadas
indices = np.where(colunas==True)
print(indices)

# Verificando acurácia utilizando a seleção de atributos. A acurácia será maior, já que os atributos foram selecionados.
naive2 = GaussianNB()
naive2.fit(X_novo,y)
previsoes2 = naive2.predict(X_novo)
print(accuracy_score(y, previsoes2))