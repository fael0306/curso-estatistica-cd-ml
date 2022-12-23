import numpy as np
import matplotlib.pyplot as plt
import math

dados = np.array([160, 165, 167, 164, 160, 166, 160, 161, 150, 152, 173, 160, 155, 164, 168, 
162, 161, 168, 163, 156, 155, 169, 151, 170, 164, 155, 152, 163, 160, 155, 157, 156, 158, 158, 
161, 154, 161, 156, 172, 153])

dados = np.sort(dados)

print(dados)

minimo = dados.min()
maximo = dados.max()

# Contando a frequência de cada valor
print(np.unique(dados, return_counts=True))

# Gerando gráfico em barras
plt.bar(dados, dados)
plt.show()

# Usando fórmula de Sturges
n = len(dados)
i = round(1+3.3*np.log10(n))
#print(i)
aa=maximo-minimo
h = aa/i
# Arredondando para cima
h = math.ceil(h)

# Criando intervalos do histograma
intervalos = np.arange(minimo, maximo+2, step=h)
print(intervalos)

# Contando quantos elementos estão dentro de cada classe manualmente
intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6 = 0,0,0,0,0,0

print(dados)

for k in range(n):
    if dados[k]>=intervalos[0] and dados[k]<intervalos[1]:
        intervalo1=intervalo1+1
    elif dados[k]>=intervalos[1] and dados[k]<intervalos[2]:
        intervalo2=intervalo2+1
    elif dados[k]>=intervalos[2] and dados[k]<intervalos[3]:
        intervalo3=intervalo3+1
    elif dados[k]>=intervalos[3] and dados[k]<intervalos[4]:
        intervalo4=intervalo4+1
    elif dados[k]>=intervalos[4] and dados[k]<intervalos[5]:
        intervalo5=intervalo5+1
    elif dados[k]>=intervalos[5] and dados[k]<intervalos[6]:
        intervalo6=intervalo6+1

listaintervalos = []
listaintervalos.append(intervalo1)
listaintervalos.append(intervalo2)
listaintervalos.append(intervalo3)
listaintervalos.append(intervalo4)
listaintervalos.append(intervalo5)
listaintervalos.append(intervalo6)
print(listaintervalos)

# Criando lista de classes para criar o gráfico
listaclasses = []
for k in range(len(listaintervalos)):
    listaclasses.append(str(intervalos[k]) + '-' + str(intervalos[k+1]))
print(listaclasses)

# Criando gráfico
plt.bar(listaclasses,listaintervalos)
plt.title("Distribuição de frequência")
plt.xlabel("Intervalos")
plt.ylabel("Valores")
plt.show()