from yellowbrick.target import FeatureCorrelation
import pandas as pd

dataset = pd.read_csv("C:\\Users\\f0fp1107\\Desktop\\Estatistica para Ciencia de Dados e Machine Learning\\Correlação e regressão\\house_prices.csv")
dataset = pd.DataFrame(dataset)
dataset.drop(labels = ['id', 'date', 'sqft_living', 'sqft_lot'], axis = 1, inplace=True)
print(dataset.columns[1:])

# Verificando correlação através do gráfico
grafico = FeatureCorrelation(labels=dataset.columns[1:16])
grafico.fit(dataset.iloc[:, 1:16].values, dataset.iloc[:, 0].values)
grafico.show()