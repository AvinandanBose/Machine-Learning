import numpy as np

n = np.arange(1,100,2)
n2 = np.arange(1,100,2)
print("n:",n)
print("n2:",n)

from matplotlib import pyplot as plt
plt.plot(n,n2)
plt.show()
