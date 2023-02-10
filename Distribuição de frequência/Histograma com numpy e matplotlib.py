import numpy as np
import matplotlib.pyplot as plt

dados = np.array([160, 165, 167, 164, 160, 166, 160, 161, 150, 152, 173, 160, 155, 164, 168, 
162, 161, 168, 163, 156, 155, 169, 151, 170, 164, 155, 152, 163, 160, 155, 157, 156, 158, 158, 
161, 154, 161, 156, 172, 153])

# Criando histograma com Numpy
frequencia, classes = np.histogram(dados)

# Verificando frequência e classes
print(frequencia, classes, len(classes))

# Gerando histograma de acordo com as classes criadas pelo Numpy
plt.hist(dados,bins=classes)
plt.show()

# Histrograma com 5 faixas de valores
frequencia, classes = np.histogram(dados, bins=5)
print(frequencia,classes)

# Gerando gráfico
plt.hist(dados,bins=classes)
plt.show()

# Histrograma usando o método de Sturges para calcular a faixa de valores
frequencia, classes = np.histogram(dados, bins='sturges')
print(frequencia,classes)

plt.hist(dados,classes)
plt.show()