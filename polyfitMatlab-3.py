import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1]

curve = np.polyfit(x,y,2)
poly = np.poly1d(curve)

new_x = []
new_y = []

for i in range(20):
    new_x.append(i+1)
    calc = poly(i+1)
    new_y.append(calc)

plt.plot(new_x,new_y)
plt.scatter(x,y)
plt.show()
