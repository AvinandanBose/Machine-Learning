import numpy as np
import matplotlib.pyplot as plt

x = [0,2,3,5,6,7,8]
y = [-2,4,3,2,4,9,12]
coefficients = np.polyfit(x,y,3) #3 is degree

print('x:',x)
print('y:',y)
print('coefficients:',coefficients)

fx = np.linspace(-1,9,100)
fy = np.polyval(coefficients,fx)

print('fx:',fx)
print('fy:',fy)

plt.plot(fx,fy,'-')
plt.plot(x,y,'ro')
plt.show()
