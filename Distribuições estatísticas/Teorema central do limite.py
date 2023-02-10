# TEOREMA CENTRAL DO LIMITE - DEFINIÇÃO
# Quando o tamanho da amostra aumenta, a distribuição amostral da sua média aproxima-se cada vez mais de uma distribuição normal

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Gerando 500 alturas aleatórias entre 126cm e 192cm
alturas = np.random.randint(126,192,500)

# Verificando gráfico das alturas geradas aleatoriamente
#sns.distplot(alturas)
#plt.show()

# Gerando 1000 vetores com 500 posições com alturas aleatórias e gerando a média de cada um deles
medias = [np.mean(np.random.randint(126, 192, 500)) for _ in range(1000)]
#print(medias)
# Verificando que essas variáveis aleatórias formam uma distribuição normal, provando o TCL
#sns.distplot(medias)
#plt.show()

# Gerando 100 vetores com 500 posições com alturas aleatórias e gerando a média de cada um deles
# Mostrando que o gráfico normal está sendo formado, porém não se aproxima tanto quanto com 1000
medias = [np.mean(np.random.randint(126, 192, 500)) for _ in range(100)]
print(medias)
#sns.distplot(medias)
#plt.show()

# Gerando 20 vetores com 500 posições com alturas aleatórias e gerando a média de cada um deles
# Mostrando que o gráfico normal está sendo formado, porém não se aproxima tanto quanto com 1000
medias = [np.mean(np.random.randint(126, 192, 500)) for _ in range(20)]
print(medias)
#sns.distplot(medias)
#plt.show()