import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

dados = np.array([126. , 129.5, 133. , 133. , 136.5, 136.5, 140. , 140. , 140. ,
                  140. , 143.5, 143.5, 143.5, 143.5, 143.5, 143.5, 147. , 147. ,
                  147. , 147. , 147. , 147. , 147. , 150.5, 150.5, 150.5, 150.5,
                  150.5, 150.5, 150.5, 150.5, 154. , 154. , 154. , 154. , 154. ,
                  154. , 154. , 154. , 154. , 157.5, 157.5, 157.5, 157.5, 157.5,
                  157.5, 157.5, 157.5, 157.5, 157.5, 161. , 161. , 161. , 161. ,
                  161. , 161. , 161. , 161. , 161. , 161. , 164.5, 164.5, 164.5,
                  164.5, 164.5, 164.5, 164.5, 164.5, 164.5, 168. , 168. , 168. ,
                  168. , 168. , 168. , 168. , 168. , 171.5, 171.5, 171.5, 171.5,
                  171.5, 171.5, 171.5, 175. , 175. , 175. , 175. , 175. , 175. ,
                  178.5, 178.5, 178.5, 178.5, 182. , 182. , 185.5, 185.5, 189., 192.5])

sns.displot(dados)
#plt.show()

# Verificando média e desvio padrão
media = np.mean(dados)
desviopadrao = np.std(dados)
print(media, desviopadrao)
# Verificando quartis
print(np.quantile(dados,[0.25,0.50,0.75]))

# Calculando probabilidade de retirar aleatoriamente alguém no primeiro quartil
valorpadronizado = (150.5-media)/desviopadrao
print(valorpadronizado)
# O resultado é -0.641025641025641
# Verificando a tabela de probabilidades da distribuição normal, podemos verificar que a probabilidade é de 26,109%

# Calculando probabilidade de retirar aleatoriamente alguém no terceiro quartil
valorpadronizado = (168-media)/desviopadrao
print(valorpadronizado)
# Verificando a tabela de probabilidades da distribuição normal, podemos verificar que a probabilidade é de (1-0,73891)%, 
# ou seja 26,109% também
print(1-0.73891)

# Calculando probabilidade de retirar aleatoriamente alguém entre o segundo e terceiro quartis
e1 = (168-media)/desviopadrao
# Verificando a tabela de probabilidades da distribuição normal, podemos verificar que a probabilidade é de (1-0,73891)%, 
# ou seja 26,109% também
e2 = (159.25-media)/desviopadrao
# Verificando a tabela de probabilidades da distribuição normal, podemos verificar que a probabilidade é de 50%, 
# pois está na mediana

# Probabilidade de selecionar uma pessoa da mediana até o terceiro quartil
print(0.73891-.5)

# Probabilidade de selecionar uma pessoa no primeiro ou terceiro quartil
# Ou seja, a soma entre as 2 probabilidades
q1ouq3 = (1-0.73891)+(1-0.73891)
print(q1ouq3)
# Probabilidade de selecionar uma pessoa que não esteja no primeiro ou terceiro quartil
# Ou seja, a soma entre as 2 probabilidades
print(1-q1ouq3)


# UTILIZANDO AS BIBLIOTECAS
# Calculando probabilidade de retirar aleatoriamente alguém no primeiro quartil
pq1 = stats.norm.cdf(150.5,media,desviopadrao)
print(pq1)
# Calculando probabilidade de retirar aleatoriamente alguém no terceiro quartil
pq3 = stats.norm.sf(168,media,desviopadrao)
print(pq3)
# Calculando probabilidade de retirar aleatoriamente alguém entre o segundo e terceiro quartil
pateq3 = stats.norm.cdf(168,media,desviopadrao)
pateq2 = stats.norm.cdf(159.25,media,desviopadrao) # Mesmo valor da mediana
pq23 = pateq3-pateq2
print(pq23)