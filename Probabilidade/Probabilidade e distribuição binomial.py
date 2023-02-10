import math
from scipy import stats

n=10
x=5
p=0.5

# Calculando manualmente
print((math.factorial(n))/(math.factorial(x)*math.factorial(n-x))*math.pow(p,x)*math.pow(1-p,n-x))

# Calculando com biblioteca
print(stats.binom.pmf(x,n,p))