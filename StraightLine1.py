from matplotlib import pyplot as plt
import time
def plot_linear_eq(m,c,clr):
    x = list(range(0,10))
    y = [(m*i + c) for i in x]
    plt.plot(x,y,label='linear',linestyle='-',color=clr)

m = float(input("Enter slope ="))
c = float(input("Enter y - intercept = "))
plot_linear_eq(m,c,'r')
plt.show()
plt.pause(5)
plt.close()
    
