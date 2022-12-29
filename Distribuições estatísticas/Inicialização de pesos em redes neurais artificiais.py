import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Random normal
normal = tf.keras.initializers.RandomNormal()
dadosnormal = normal(shape=[1000])
print(np.mean(dadosnormal),np.std(dadosnormal))
#sns.distplot(dadosnormal)
#plt.show()

# Random uniform
uniforme = tf.keras.initializers.RandomUniform()
dadosuniforme = uniforme(shape=[1000])
#sns.distplot(dadosuniforme)
#plt.show()

# Glorot normal
normalglorot = tf.keras.initializers.GlorotNormal()
dadosnormalglorot = normalglorot(shape=[1000])
#sns.distplot(dadosnormalglorot)
#plt.show()

# Glorot uniforme
uniformeglorot = tf.keras.initializers.GlorotUniform()
dadosuniformeglorot = uniformeglorot(shape=[1000])
#sns.distplot(dadosnormalglorot)
#plt.show()