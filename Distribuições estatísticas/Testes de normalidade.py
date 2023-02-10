from scipy import stats
from scipy.stats import skewnorm
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro

# Gerando dados normais e não normais
dadosnormais = stats.norm.rvs(size=1000)
dadosnaonormais = skewnorm.rvs(a=10, size=1000)

# Gerando histograma para verificar se os dados são ou não normais através do enviesamento (maneira visual)
sns.distplot(dadosnormais)
#plt.show()
sns.distplot(dadosnaonormais)
#plt.show()

# Verificando se os dados são normais através dos quartis. Quando os pontos estão próximos da linha, é normal.
qqplot(dadosnormais, line='s')
#plt.show()
qqplot(dadosnaonormais, line='s')
#plt.show()

# Teste de Shapiro-Wilk
_, p = shapiro(dadosnormais)
#print(p)

alpha = 0.05
if p>alpha:
    print("Distribuição normal.")
else:
    print("Distribuição não normal.")

_, p = shapiro(dadosnaonormais)
#print(p)
alpha = 0.05
if p>alpha:
    print("Distribuição normal.")
else:
    print("Distribuição não normal.")