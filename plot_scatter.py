from matplotlib import pyplot as plt
import time
def plot_scatter(a,b,c1,m,c):
    x = list(range(0,10))
    x1 = list(range(0,10))
    y= [(m*i + c) for i in x] #straightLine
    y1 = [(a+b*i+c1*i**2) for i in x1] #polynomial
    plt.plot(x,y,label='linear',linestyle='-',color='r')
    plt.scatter(x1,y1,color='b')
    
m = float(input("Enter slope ="))
c = float(input("Enter y - intercept = "))
a = float(input("Enter a ="))
b = float(input("Enter b = "))
c1 = float(input("Enter c1 ="))
plot_scatter(a,b,c1,m,c)
plt.grid()
plt.show()
plt.pause(5)
plt.close()

