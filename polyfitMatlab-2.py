import matplotlib.pyplot as plt
import numpy as np

x = 3* np.random.random(25)
noise = 3* np.random.random(x.size)**2
y= 5*x**2-12*x+7+5*noise

print('x:',x)
print('noise:',noise)
print('y:',y)

for degree in [1,2,5,10]:
    coefficients = np.polyfit(x,y,degree)
    fx= np.linspace(-1,4,100)
    fy= np.polyval(coefficients,fx)
    plt.plot(fx,fy,'-',label="degree %s" % degree)

avg = np.average(y)
plt.plot(x,y,'ro')
plt.plot([-1,4],[avg,avg],'k-',label="average")
plt.ylim(-3,15)
plt.title('Least squares polynomial fit')
plt.legend()
plt.show()

