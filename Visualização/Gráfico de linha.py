import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

vendas = {'Mês':np.array([1,2,3,4,5,6,7,8,9,10,11,12]),
          'Valor':np.array([100,200,120,300,500,198,200,209,130,500,300,120])}

vendasdf = pd.DataFrame(vendas)
#print(vendasdf)

sns.relplot(x="Mês", y="Valor", kind="line", data=vendasdf)
plt.show()