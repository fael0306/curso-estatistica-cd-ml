import math
import pandas as pd

# Criando dicionário com as frequências
dados = {"Inferior":[150,154,158,162,166,170],
         "Superior":[154,158,162,166,170,174],
         "fi":[5,9,11,7,5,3]}

# Criando a tabela usando o dicionário
dataset = pd.DataFrame(dados)

# Criando novo campo xi (ponto médio das classes)
dataset["xi"]=(dataset["Superior"]+dataset["Inferior"])/2

# Criando campo que multiplica as frequências e as médias para depois gerar a média
dataset["fi.xi"]=(dataset["fi"]*dataset["xi"])

# Criando campo da frequência acumulada
dataset["Fi"]=0
fqacumulada = []
cont = 0
for linha in dataset.iterrows():
    cont=cont+linha[1][2]
    fqacumulada.append(cont)
dataset["Fi"]=fqacumulada
#print(dataset)


# Calculando desvio padrão manualmente

# Elevando os dados ao quadrado, conforme a fórmula do desvio padrão
dataset["xi_2"]=dataset["xi"]**2

# Multiplicando a frequência de cada um pelo seu respectivo x², conforme a fórmula do desvio padrão
dataset["fi_xi_2"]=dataset["xi_2"]*dataset["fi"]

# Modificando a ordem das colunas do dataset
#print(dataset.columns)

# Criando lista com a ordem requerida das colunas
colunasordenadas = ['Inferior', 'Superior', 'fi', 'xi', 'fi.xi', 'xi_2', 'fi_xi_2', 'Fi']

# Recebendo as colunas ordenadas
dataset = dataset[colunasordenadas]

# Calculando desvio padrão pela fórmula
dp = math.sqrt(dataset["fi_xi_2"].sum()/dataset["fi"].sum()-math.pow(dataset["fi.xi"].sum()/dataset["fi"].sum(),2))
print(dp)