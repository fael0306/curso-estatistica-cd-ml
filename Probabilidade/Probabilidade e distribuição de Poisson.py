import math
from scipy import stats

x = 14
media = 10

# Aplicando a fórmula de Poisson manualmente
p = math.pow(math.e, -media)*(math.pow(media,x)/math.factorial(x))*100
print(p)

# Usando a biblioteca
p = stats.poisson.pmf(x, media)*100
print(p)