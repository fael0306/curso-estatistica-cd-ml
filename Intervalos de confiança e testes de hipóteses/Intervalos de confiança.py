import numpy as np
from scipy.stats import norm
from scipy import stats
import seaborn as sns
import math
import matplotlib.pyplot as plt

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

n = len(dados)
media = np.mean(dados)
desviopadrao = np.std(dados)

# Intervalo de confiança manual (95%)
alpha = (1-0.95)/2
z = 1-alpha
# Para 99% de confiança
# limiteinferior = media - 2.575*desviopadrao()/sqrt(qtddevalores)
# limitesuperior = media - 2.575*desviopadrao()/sqrt(qtddevalores)
# Para 95% de confiança
# limiteinferior = media - 1.96*desviopadrao()/sqrt(qtddevalores)
# limitesuperior = media - 1.96*desviopadrao()/sqrt(qtddevalores)

# Usando biblioteca
z = norm.ppf(1-alpha)
xinferior = media-z*(desviopadrao/math.sqrt(n))
xsuperior = media+z*(desviopadrao/math.sqrt(n))
print(xinferior,xsuperior)
margemerro = media-xinferior
print(margemerro)

# Gerando gráfico dos dados
sns.distplot(dados)
#plt.show()

# Usando Scipy
# stats.sem(dados) = desviopadrao/math.sqrt(n-1) -> -1 pois começa no 0
intervalos = norm.interval(0.95, media, stats.sem(dados))
print(intervalos)
margemerro = media-intervalos[0]
print(margemerro)

# Usando diferentes níveis de confiança
intervalos = norm.interval(0.99, media, stats.sem(dados)) # 99% de certeza que a média está entre os valores do intervalo
print(intervalos)
margemerro = media-intervalos[0]
print(margemerro)
intervalos = norm.interval(0.95, media, stats.sem(dados)) # 95% de certeza que a média está entre os valores do intervalo
print(intervalos)
margemerro = media-intervalos[0]
print(margemerro)
intervalos = norm.interval(0.90, media, stats.sem(dados)) # 90% de certeza que a média está entre os valores do intervalo
print(intervalos)
margemerro = media-intervalos[0]
print(margemerro)