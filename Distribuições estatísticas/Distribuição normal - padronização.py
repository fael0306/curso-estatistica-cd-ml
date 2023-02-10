import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Gerando dados em formato normal já padronizados (na mesma escala)
dadosnormalpadronizado = np.random.standard_normal(size=1000)

#sns.distplot(dadosnormalpadronizado)
#plt.show()

# Verificando se os dados estão coerentes com uma distribuição normal padronizado
# Média ~ 0 e Desvio Padrão ~ 1
print(dadosnormalpadronizado.mean(), np.std(dadosnormalpadronizado))


# Padronizando dados através da fórmula
# Z = (x - média)/desvio padrão
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

# Encontrando variáveis da fórmula
media = dados.mean()
print(media)
dp = np.std(dados)

# Rodando registros e aplicando fórmula e gerando novos dados
dadospadronizados = (dados-media)/dp
print(dadospadronizados)

# Verificando se os dados estão coerentes com uma distribuição normal padronizado
# Média ~ 0 e Desvio Padrão ~ 1
print(dadospadronizados.mean(), np.std(dadospadronizados))

#sns.histplot(dadospadronizados)
#plt.show()