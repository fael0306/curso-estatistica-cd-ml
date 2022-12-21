import pandas as pd

# Criando dicionário com as frequências
dados = {"Inferior":[150,154,158,162,166,170],
         "Superior":[154,158,162,166,170,174],
         "fi":[5,9,11,7,5,3]}

# Criando a tabela usando o dicionário
dataset = pd.DataFrame(dados)
print(dataset)

# Criando novo campo xi (ponto médio das classes)
dataset["xi"]=(dataset["Superior"]+dataset["Inferior"])/2
print(dataset)

# Criando campo que multiplica as frequências e as médias para depois gerar a média
dataset["fi.xi"]=(dataset["fi"]*dataset["xi"])
print(dataset)

# Criando campo da frequência acumulada
dataset["Fi"]=0
fqacumulada = []
cont = 0
for linha in dataset.iterrows():
    cont=cont+linha[1][2]
    fqacumulada.append(cont)
print(fqacumulada)
dataset["Fi"]=fqacumulada
print(dataset)

# Fazendo a média ponderada
mediaponderada = dataset["fi.xi"].sum()/dataset["fi"].sum()
print(mediaponderada)

# Encontrando a linha que é moda. A moda recebe aquele campo que é igual ao máximo.
moda=dataset[dataset["fi"]==dataset["fi"].max()]["xi"].values[0]
print(moda)

# Encontrando classe da mediana
fi2 = dataset["fi"].sum()/2
print(fi2)

# Criando função
def quartil(dataframe):
    for linha in dataset.iterrows():
        #print(linha)
        limiteinf = linha[1][0]
        fqclasse = linha[1][2]
        idfreqant = linha[0]
        if linha[1][5]>=fi2:
            idfreqant = idfreqant-1
            break
    print(limiteinf, fqclasse, idfreqant)

    # Encontrando frequência acumulada anterior
    fiant = dataset.iloc[[idfreqant]]["Fi"].values[0]
    print(fiant)

    # Calculando mediana pela fórmula - o intervalo é 4
    mediana = limiteinf+((fi2-fiant)*4)/fqclasse
    return mediana

print(quartil(dados))