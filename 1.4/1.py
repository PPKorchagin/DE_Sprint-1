from matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,10,0.1)

for o in [0.5,1,2,4]:
  y=(x/o**2)*np.exp(-(x**2)/(2*o**2))
  plt.plot(x,y, label=f"o={o}")
plt.legend()
plt.show()