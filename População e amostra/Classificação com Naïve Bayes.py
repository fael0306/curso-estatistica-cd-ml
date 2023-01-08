import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\credit_data.csv")

print(dataset.shape)
print(dataset.head())

# Apagando registros vazios para evitar erros
dataset.dropna(inplace=True)
print(dataset.shape)

# Plotando
sns.countplot(dataset['c#default'])
plt.show()

# Alocando as colunas 0, 1 e 2 em x
x = dataset.iloc[:, 1:4].values

# Monstrando quantidades de (registros, colunas)
print(x.shape)

# Mostrando tabela
print(x)

# Alocando a primeira coluna
y = dataset.iloc[:, 4].values

# Mostrando quantidades de (registros, colunas)
print(y.shape)

# Mostrando tabela
print(y)

from sklearn.model_selection import train_test_split

# Criando amostra estratificada usando 20% da base de dados
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(x, y, test_size=0.2, stratify=y)

# Verificando tamanho das variáveis
print(X_treinamento.shape)
print(y_treinamento.shape)
print(X_teste.shape)
print(y_teste.shape)

# Encontrando quantidade de valores de cada classe
print(np.unique(y, return_counts=True))

# Verificando proporção
print(1714/len(dataset))
print(283/len(dataset))

# Vericando proporção
print(np.unique(y_treinamento, return_counts=True))
print(np.unique(y_teste, return_counts=True))

# Verificando se a proporção está correta
print(226/len(y_treinamento))
print(57/len(y_teste))

from sklearn.naive_bayes import GaussianNB

modelo = GaussianNB()

# Encaixando o algoritmo Naive Bayes nos dados obtidos
modelo.fit(X_treinamento,y_treinamento)

# Retornando previsões (se a pessoa paga ou não o empréstimo). Necessário comparar se bate com os dados da base y_teste para verificar acerto de previsão
previsoes = modelo.predict(X_teste)

print(previsoes)
print(y_teste)

from sklearn.metrics import accuracy_score

# Verificando taxa de acerto das previsões
print("A taxa de acerto da previsão é:",accuracy_score(previsoes, y_teste)*100,"%")

from sklearn.metrics import confusion_matrix

# Matriz de classificações 
# pagam empréstimo e foram classificados corretamente, pagam empréstimo e foram classificados incorretamente 
# não pagam e foram classificados como pagantes, não pagam e foram classificados corretamente
cm = confusion_matrix(previsoes, y_teste)
print(cm)

# Pegando os elementos da matriz
matrizlista = cm.tolist()

# Gráfico da matriz
sns.heatmap(cm, annot=True)
plt.show()

# Percentual de acerto para pessoas que pagam o empréstimo: primeiro elemento da primeira linha são os acertos e a primeira linha são os que pagam, então dividimos os acertos pelo total da linha
print("Percentual de acerto para pessoas que pagam o empréstimo:",round(matrizlista[0][0]/sum(matrizlista[0])*100,2),"%")

# Percentual de acerto para pessoas que não pagam o empréstimo: segundo elemento da segunda linha são os acertos e a segunda linha são os que não pagam, então dividimos os acertos pelo total da linha
print("Percentual de acerto para pessoas que não pagam o empréstimo:",round(matrizlista[1][1]/sum(matrizlista[1])*100,2),"%")

# O acerto é bem maior para o caso que acontece mais, já que a previsão melhora com a quantidade de dados a mais
