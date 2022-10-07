from matplotlib import pyplot as plt
import numpy as np

x=np.arange(-2,2,0.0001)
x2=x**2
x43=(x**4)**(1/3)
x23=(x**2)**(1/3)
sq=np.sqrt(x43-x2+1)

y1=x23/2+sq
y2=x23/2-sq


plt.plot(x,y1,c='r')
plt.plot(x,y2,c='r')

plt.show()
