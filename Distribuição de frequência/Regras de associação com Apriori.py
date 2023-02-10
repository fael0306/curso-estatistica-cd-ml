import pandas as pd

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\População e Amostra\\census.csv")

print(dataset.head())

# Pegando colunas específicas da tabela
dataset_apriori = dataset[["income","age","hour-per-week"]]
print(dataset_apriori.head())

#print(dataset_apriori.shape)

# Utilizando a técnica de amostragem simples com 99% de confiança (SurveyMonkey)
dataset_apriori = dataset_apriori.sample(n=500)
print(dataset_apriori.shape)
print(dataset_apriori.head())

# Transformando dataset em lista
transacoes = []
for i in range(dataset_apriori.shape[0]):
    transacoes.append([str(dataset_apriori.values[i,j]) for j in range(dataset_apriori.shape[1])])
print(len(transacoes))

# Verificando os 2 primeiros registros
#print(transacoes[:2])

from apyori import apriori

# Criando regras de associação das variáves da tabela
regras = apriori(transacoes, min_support=0.3, min_confidence=0.2)
resultados = list(regras)

# Verificando regras criadas
#print(resultados)
print(resultados[2])