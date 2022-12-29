from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Distribuições estatísticas\\census.csv")

print(dataset.head())

from sklearn.preprocessing import LabelEncoder
# Criando um objeto para cada atributo
labelencoder0 = LabelEncoder()
labelencoder1 = LabelEncoder()
labelencoder2 = LabelEncoder()
labelencoder3 = LabelEncoder()
labelencoder4 = LabelEncoder()
labelencoder5 = LabelEncoder()
labelencoder6 = LabelEncoder()

# Transformando atributos em números
dataset['workclass'] = labelencoder0.fit_transform(dataset['workclass'])
dataset['education'] = labelencoder1.fit_transform(dataset['education'])
dataset['marital-status'] = labelencoder1.fit_transform(dataset['marital-status'])
dataset['occupation'] = labelencoder1.fit_transform(dataset['occupation'])
dataset['relationship'] = labelencoder1.fit_transform(dataset['relationship'])
dataset['race'] = labelencoder1.fit_transform(dataset['race'])
dataset['native-country'] = labelencoder1.fit_transform(dataset['native-country'])

#print(dataset.head())

# Transformando em listas
X = dataset.iloc[:, [1,3,5,7,8,13]].values
print(X)
y = dataset['income'].values
print(y)

# Criando previsões
multinomialnayvebayes = MultinomialNB()
multinomialnayvebayes.fit(X,y)
previsoes = multinomialnayvebayes.predict(X)
print(previsoes,y)
# Calculando acurácia das previsões
print(accuracy_score(y, previsoes))