import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
 
#Fitting function
def func(x, a, b):
    return a*np.exp(b*x)
    
 
#Experimental x and y data points    
xData = np.array([1, 2, 3, 4, 5])
yData = np.array([1, 9, 50, 300, 1500])
 
#Plot experimental data points
plt.plot(xData, yData, 'bo', label='experimental-data')
 
# Initial guess for the parameters
initialGuess = [1.0,1.0]    
 
#Perform the curve-fit
popt,pcov = curve_fit(func, xData, yData, initialGuess)
print(popt)
print(pcov)
 
#x values for the fitted function
xFit = np.arange(0.0, 5.0, 0.01)
 
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
