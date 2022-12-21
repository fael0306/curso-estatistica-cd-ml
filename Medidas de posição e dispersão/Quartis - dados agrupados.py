import pandas as pd

# Criando dicionário com as frequências
dados = {"Inferior":[150,154,158,162,166,170],
         "Superior":[154,158,162,166,170,174],
         "fi":[5,9,11,7,5,3]}

# Criando a tabela usando o dicionário
dataset = pd.DataFrame(dados)
#print(dataset)

# Criando novo campo xi (ponto médio das classes)
dataset["xi"]=(dataset["Superior"]+dataset["Inferior"])/2
#print(dataset)

# Criando campo que multiplica as frequências e as médias para depois gerar a média
dataset["fi.xi"]=(dataset["fi"]*dataset["xi"])
#print(dataset)

# Criando campo da frequência acumulada
dataset["Fi"]=0
fqacumulada = []
cont = 0
for linha in dataset.iterrows():
    cont=cont+linha[1][2]
    fqacumulada.append(cont)
#print(fqacumulada)
dataset["Fi"]=fqacumulada
print(dataset)

# Criando função
def quartil(dataframe, q1 = True):
    if q1==True:
        fi_4 = dataset["fi"].sum()/4
    else:
        fi_4 = (3*dataset["fi"].sum())/4
    for linha in dataset.iterrows():
        #print(linha)
        limiteinf = linha[1][0]
        fqclasse = linha[1][2]
        idfreqant = linha[0]
        if linha[1][5]>=fi_4:
            idfreqant = idfreqant-1
            break
    #print(limiteinf, fqclasse, idfreqant)

    # Encontrando frequência acumulada anterior
    fiant = dataset.iloc[[idfreqant]]["Fi"].values[0]
    #print(fiant)

    # Calculando mediana pela fórmula - o intervalo é 4
    mediana = limiteinf+((fi_4-fiant)*4)/fqclasse
    return mediana

print(quartil(dados),quartil(dados, q1 = True))
print(quartil(dados),quartil(dados, q1 = False))