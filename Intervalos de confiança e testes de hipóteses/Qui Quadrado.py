from scipy.stats import chi2_contingency
import numpy as np

tabela = np.array([[30,20],[22,28]])

print(tabela.shape)

# Calculando o Qui Quadrado (o segundo parâmetro é o mais importante)
#print(chi2_contingency(tabela))

# Pegando apenas o segundo parâmetro
_, p, _, _ = chi2_contingency(tabela)
#print(p)

# Não há diferença estatística entre o conjunto de dados, por isso será rejeitada
alpha = 0.05
if(p<=alpha):
    print("Hipótese nula rejeitada.")
else:
    print("Hipótese alternativa rejeitada")

# Mudando a tabela para gerar diferenças grandes entre os valores
tabela = np.array([[45,5],[5,45]])

# Pegando apenas o segundo parâmetro
_, p, _, _ = chi2_contingency(tabela)

# NEsse caso há diferença estatística significativa entre os dados
if(p<=alpha):
    print("Hipótese nula rejeitada.")
else:
    print("Hipótese alternativa rejeitada")