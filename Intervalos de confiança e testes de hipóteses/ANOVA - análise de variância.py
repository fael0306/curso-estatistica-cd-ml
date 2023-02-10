import numpy as np

grupoa = np.array([165, 152, 143, 140, 155])
grupob = np.array([130, 169, 164, 143, 154])
grupoc = np.array([163, 158, 154, 149, 156])

from scipy.stats import f

print(f.ppf(1-0.05, dfn = 2, dfd = 12))

from scipy.stats import f_oneway

# Vai retornar o valor de p
_, p = f_oneway(grupoa, grupob, grupoc)
print(p)

alpha = 0.05

if p<=alpha:
    print("Hipótese nula rejeitada.")
else:
    print("Hipótese alternativa rejeitada.")

# Teste de Tukey
dados = {'Valores':[165, 152, 143, 140, 155, 130, 169, 164, 143, 154, 163, 158, 154, 149, 156],
         'Grupo':['A','A','A','A','A','B','B','B','B','B','C','C','C','C','C']}

import pandas as pd
dados = pd.DataFrame(dados)

from statsmodels.stats.multicomp import MultiComparison

# A coluna reject vai informar se rejeita a hipótese nula
comparagrupos = MultiComparison(dados['Valores'], dados['Grupo'])
teste = comparagrupos.tukeyhsd()
print(teste)

import matplotlib.pyplot as plt

# Verificando médias de grupos através de gráfico
teste.plot_simultaneous()
#plt.show()

# Testando com outros dados no grupo A, fazendo com que ele fique bem diferente
dados = {'Valores':[70, 90, 80, 50, 20, 130, 169, 164, 143, 154, 163, 158, 154, 149, 156],
         'Grupo':['A','A','A','A','A','B','B','B','B','B','C','C','C','C','C']}

dados = pd.DataFrame(dados)

# A coluna reject vai informar se rejeita a hipótese nula
comparagrupos = MultiComparison(dados['Valores'], dados['Grupo'])
teste = comparagrupos.tukeyhsd()
print(teste)

# Verificando médias de grupos através de gráfico
teste.plot_simultaneous()
#plt.show()