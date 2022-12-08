import pandas as pd

dados = {'Emprego': ['Administrador de Banco de Dados','Programador','Arquiteto de Redes'],
'Nova Jersey':[97350, 82080, 112840],
'Flórida':[77140,71540,62310]}

print(type(dados))

print(dados)

dataset = pd.DataFrame(dados)

#print(dataset)

print(dataset['Nova Jersey'].sum())
print(dataset['Flórida'].sum())

# Criando nova coluna com o percentual de Nova Jersey
dataset['% Nova Jersey'] = round((dataset['Nova Jersey']/dataset['Nova Jersey'].sum())*100,2)

# Criando nova coluna com o percentual da Flórida
dataset['% Flórida'] = round((dataset['Flórida']/dataset['Flórida'].sum())*100,2)

print(dataset)