from matplotlib import pyplot as plt
import time
def parabola(a,b,c,clr):
    x = list(range(0,10))
    y = [(a+b*i+c*i**2) for i in x]
    plt.scatter(x,y,color=clr)
    plt.plot(x,y,color=clr)
a = float(input("Enter a ="))
b = float(input("Enter b = "))
c = float(input("Enter c ="))
parabola(a,b,c,'b')
plt.show()
plt.pause(5)
plt.close()
