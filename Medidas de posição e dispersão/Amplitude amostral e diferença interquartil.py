import numpy as np

dados = np.array([150, 151, 152, 152, 153, 154, 155, 155, 155, 155, 156, 156, 156, 157, 158, 158, 160, 160, 160, 160, 160, 
161, 161, 161, 161, 162, 163, 163, 164, 164, 164, 165, 166, 167, 168, 168, 169, 170, 172, 173])

# Calculando amplitude amostral
print(dados.max()-dados.min())

# Quartil 1 e 3
q1 = np.quantile(dados, 0.25)
q3 = np.quantile(dados, 0.75)
print(q1,q3)

# Calculando diferença interquartil
di = q3-q1
print(di)

# Calculando outliers
ci = q1-(1.5*di)
cs = q3+(1.5*di)
print(ci,cs)