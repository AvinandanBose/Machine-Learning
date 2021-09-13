import numpy as np

n = np.logspace(start=0,stop=10)# base by default 10.0
print("n=",n)

n1 = np.logspace(start=0,stop=10, num =25,base=2)
print("n1=",n1)

n2 = np.logspace(start=0,stop=10, num =25,base=3)
print("n2=",n1)

from matplotlib import pyplot as plt

plt.plot(n1,n2)
plt.show()


