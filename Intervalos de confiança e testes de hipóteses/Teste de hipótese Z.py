import numpy as np
import math
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

dadosoriginais = np.array([126. , 129.5, 133. , 133. , 136.5, 136.5, 140. , 140. , 140. ,
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

# Hipótese nula ou valor pré-existente
H0media = np.mean(dadosoriginais)
print(H0media)
H0desviopadrao = np.std(dadosoriginais)
print(H0desviopadrao)

# Supondo que 1 ano depois a mesma pesquisa é feita e o resultado da média varia 3%
dadosnovos = dadosoriginais*1.03
print(dadosnovos)
H1media = np.mean(dadosnovos)
print(H1media)
H1desviopadrao = np.std(dadosnovos)
print(H1desviopadrao)

# Quantidade de valores e nível de confiança
H1n = len(dadosnovos)
alpha = 0.05

# Teste manual
Z = (H1media-H0media)/(H1desviopadrao/math.sqrt(H1n))
print(Z)

# Verificando o valor na tabela através da biblioteca
print(norm.cdf(Z))
# Passando para Z o valor da tabela
Z = norm.cdf(Z)

p = 1-Z
print(p)

if(p<alpha):
    print("Hipótese nula rejeitada.")
else:
    print("Hipótese alternativa rejeitada.")

# Teste com statsmodels
# Achando valor do p
_, p = ztest(dadosoriginais, dadosnovos, value = H1media-H0media, alternative='larger')
print(p)