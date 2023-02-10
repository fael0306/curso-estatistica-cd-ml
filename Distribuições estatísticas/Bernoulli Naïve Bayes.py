from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Distribuições estatísticas\\census.csv")

print(dataset['sex'].unique())

X = dataset['sex'].values
print(X)

# Transformando os valores em números
labelencoder = LabelEncoder()
X = labelencoder.fit_transform(X)
print(X)
#sns.distplot(X, kde=False)
#plt.show()

# Transformando em matriz para utilizar o Nayve Bayes
X = X.reshape(-1,1)
y = dataset['income'].values
# Prevendo o resultado com o NayveBayes
bernoullinayvebayes = BernoulliNB()
bernoullinayvebayes.fit(X,y)
previsoes = bernoullinayvebayes.predict(X)
print(previsoes, y)

# Verificando acurácia
print(accuracy_score(y, previsoes))