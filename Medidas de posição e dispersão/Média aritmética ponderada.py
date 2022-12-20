import numpy as np

notas = np.array([9,8,7,3])
pesos = np.array([1,2,3,4])

# Manual
print(9*1+8*2+7*3+3*4)

# Usando Numpy
mediaponderada = (notas*pesos).sum()/pesos.sum()
print(mediaponderada)

print(np.average(notas, weights=pesos))