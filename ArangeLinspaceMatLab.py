import numpy as np
import matplotlib.pyplot as plt

N = 25
#LinSpace(startpoint , endpoint)
x = list(np.linspace(start=0,stop=10,num=25,endpoint=False))

y = list(np.arange(start=0,stop=25))

print("x:",x)
print("y:",y)

plt.plot(x,y)
plt.show()
