import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

   
x = np.array([1, 2, 3, 4, 5])

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))


def func(x, a, b):
    return a*np.log(x)+b

y = func(x,a,b)

plt.plot(x, y, 'bo', label='experimental-data')


initialGuess = [1.0,1.0]
popVal,popZero  = curve_fit(func, x, y,initialGuess)
print(popVal)

xFit = np.arange(0.0, 5.0, 0.01)

plt.plot(xFit, func(xFit, *popVal),'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popVal))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
