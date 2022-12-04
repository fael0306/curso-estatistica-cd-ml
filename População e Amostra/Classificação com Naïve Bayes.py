import pandas as pd
import seaborn as sns
import numpy as np

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\credit_data.csv")

print(dataset.shape)
print(dataset.head())

# Apagando registros vazios para evitar erros
dataset.dropna(inplace=True)
print(dataset.shape)

# Plotando, porém, só plota no Colab
sns.countplot(dataset['c#default'])

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
soma = 0
for i in range(400):
    if previsoes[i]==y_teste[i]:
        soma = soma+1
# Printando taxa de acerto
print("")
print("Taxa de acerto da previsão:",soma/len(previsoes)*100,"%")