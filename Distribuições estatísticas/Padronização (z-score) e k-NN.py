import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("C:\\Users\\f0fp1107\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Distribuições estatísticas\\credit_data.csv")

# Apagando dados vazios
dataset.dropna(inplace=True)
print(dataset.head())

# Sem padronização
X = dataset.iloc[:, 1:4].values
y = dataset["c#default"].values
# Gerando as variáveis de teste e treinamento (20% para testar e 80% para treinar)
Xtreinamento, Xteste, ytreinamento, yteste = train_test_split(X, y, test_size=0.2, stratify=y)
# Verificando estatísticas dos salários
print(np.mean(Xtreinamento[0]), np.median(Xtreinamento[0]), np.std(Xtreinamento[0]))
print(np.mean(Xteste[0]), np.median(Xteste[0]), np.std(Xteste[0]))
# Criando previsões
knn = KNeighborsClassifier()
knn.fit(Xtreinamento, ytreinamento)
previsoes = knn.predict(Xteste)
# Verificando acurácia
print(accuracy_score(yteste, previsoes))

# Com padronização
zscoretreinamento = StandardScaler()
zscoreteste = StandardScaler()
Xtreinamentop = zscoretreinamento.fit_transform(Xtreinamento)
Xtestep = zscoreteste.fit_transform(Xteste)
# Verificando mínimo e máximo
print(min(Xtreinamentop[0]),max(Xtreinamentop[0]))
# Verificando estatísticas
print(np.mean(Xtreinamentop[0]), np.median(Xtreinamentop[0]), np.std(Xtreinamentop[0]))
print(np.mean(Xtestep[0]), np.median(Xtestep[0]), np.std(Xtestep[0]))
print(np.mean(Xtreinamentop), np.median(Xtreinamentop), np.std(Xtreinamentop))
print(np.mean(Xtestep), np.median(Xtestep), np.std(Xtestep))
# Criando previsões
knn = KNeighborsClassifier()
knn.fit(Xtreinamentop,ytreinamento)
previsoes = knn.predict(Xtestep)
# Verificando acurácia
print(accuracy_score(yteste, previsoes))