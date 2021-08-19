from matplotlib import pyplot as plt
import time
def plot_linear_eq(m1,c1,m2,c2,clr):
    x0 = list(range(0,10))
    y0 = [(m1*i + c1) for i in x0]
    x1 = list(range(0,10))
    y1 = [(m2*i + c2) for i in x1]
    plt.plot(x0,y0,x1,y1,label='linear',linestyle='-',color=clr)

m0 = float(input("Enter slope0 ="))
c0 = float(input("Enter y0 - intercept = "))
m1 = float(input("Enter slope1 ="))
c1 = float(input("Enter y1 - intercept = "))
plot_linear_eq(m0,c0,m1,c1,'r')
plt.show()
plt.pause(5)
plt.close()

    
