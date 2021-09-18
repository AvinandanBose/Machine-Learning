import numpy as np

p = [3,2,1]
x = [5,7,9]
x1 = np.poly1d(p)
y = np.polyval(p,x)
print(x1)
print(y)
