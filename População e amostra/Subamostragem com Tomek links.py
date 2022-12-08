from imblearn.under_sampling import TomekLinks
import pandas as pd
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\credit_data.csv")

# Alocando as colunas 0, 1 e 2 em x
x = dataset.iloc[:, 1:4].values

# Alocando a primeira coluna
y = dataset.iloc[:, 4].values

# Linhas comentadas abaixo não funcionam pois existem valores NaN na base de dados
tl = TomekLinks(sampling_strategy='majority')
#X_under, y_under = tl.fit_resample(x, y) #Atualizado 20/05/2022

#print(X_under.shape, y_under.shape, id_under)

print(np.unique(y, return_counts=True))
# A linha abaixo mostrará que há os menos registros em y e y_under
#print(np.unique(y_under, return_counts=True))

#X_treinamento_u, X_teste_u, y_treinamento_u, y_teste_u = train_test_split(X_under, y_under, test_size = 0.2, stratify = y_under)
#X_treinamento_u.shape, X_teste_u.shape

#modelo_u = GaussianNB()
#modelo_u.fit(X_treinamento_u, y_treinamento_u)
#previsoes_u = modelo_u.predict(X_teste_u)
#accuracy_score(previsoes_u, y_teste_u)

#cm_u = confusion_matrix(previsoes_u, y_teste_u)
#print(mc_u)

print(315/(315+26)*100,"%")
print(31/(31+8)*100,"%")