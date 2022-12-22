import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from scipy import stats

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Medidas de posição e dispersão\\credit_data.csv")

# Apagando registros vazios
dataset.dropna(inplace=True)

print(dataset.shape)
print(dataset)

# Colocando registros das colunas 1 a 3 no X
X = dataset.iloc[:, 1:4].values
print(X)

# Colocando registros da coluna 4 no y
y = dataset.iloc[:, 4].values
print(y)

resultadosnaivebayes = []
resultadoslogistica = []
resultadosforest = []

# Será executado cada algoritmo de previsão 30 vezes
for i in range(30):
    
    # Gerando amostra estratificada
    X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, stratify=y, random_state=i)

    # Usando Naive Bayes
    naive_bayes = GaussianNB()
    naive_bayes.fit(X_treinamento, y_treinamento)
    resultadosnaivebayes.append(accuracy_score(y_teste, naive_bayes.predict(X_teste)))

    # Usando regressão logística
    logistica = LogisticRegression()
    logistica.fit(X_treinamento, y_treinamento)
    resultadoslogistica.append(accuracy_score(y_teste, logistica.predict(X_teste)))

    # Usando Random Forest
    randomforest = RandomForestClassifier()
    randomforest.fit(X_treinamento, y_treinamento)
    resultadosforest.append(accuracy_score(y_teste, randomforest.predict(X_teste)))

print(resultadosnaivebayes)
print(resultadoslogistica)
print(resultadosforest)

# Transformando os resultados em array do Numpy
resultadosnaivebayes = np.array(resultadosnaivebayes)
resultadoslogistica = np.array(resultadoslogistica)
resultadosforest = np.array(resultadosforest)

# Comparando os algoritmos pelas estatísticas de cada um

# Média
print(resultadosnaivebayes.mean(), resultadoslogistica.mean(), resultadosforest.mean())

# Moda
print(stats.mode(resultadosnaivebayes), stats.mode(resultadoslogistica), stats.mode(resultadosforest))

# Mediana
print(np.median(resultadosnaivebayes), np.median(resultadoslogistica), np.median(resultadosforest))

# Variância
print(np.var(resultadosnaivebayes), np.var(resultadoslogistica), np.var(resultadosforest))

# Desvio padrão
print(np.std(resultadosnaivebayes), np.std(resultadoslogistica), np.std(resultadosforest))

# Coeficiente de variação
print(stats.variation(resultadosnaivebayes)*100, stats.variation(resultadoslogistica)*100, stats.variation(resultadosforest)*100)