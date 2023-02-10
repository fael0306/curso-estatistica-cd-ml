import folium
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\house_prices.csv")
dataset = pd.DataFrame(dataset)

print(dataset.head())

lat,long = dataset['lat'].mean(), dataset['long'].mean()

mapa = folium.Map(location=[lat,long])
#mapa.save("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\mapa.html")
mapa.show_in_browser()

# Ordenando por preço e pegando as 1000 casas mais caras
dataset = dataset.sort_values(by='price', ascending=False)
datasetcaros = dataset[0:1000]

lat,long = datasetcaros['lat'].mean(), datasetcaros['long'].mean()

mapa = folium.Map(location=[lat,long])
# Para salvar podemos usar o save
#mapa.save("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\mapa.html")
# Usando este método, podemos visualizar direto no navegador
mapa.show_in_browser()

# Ordenando por preço e pegando as 1000 casas mais baratas
dataset = dataset.sort_values(by='price', ascending=True)
datasetbaratos = dataset[0:1000]

lat,long = datasetbaratos['lat'].mean(), datasetbaratos['long'].mean()

mapa = folium.Map(location=[lat,long])
# Para salvar podemos usar o save
#mapa.save("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Visualização\\mapa.html")
# Usando este método, podemos visualizar direto no navegador
mapa.show_in_browser()