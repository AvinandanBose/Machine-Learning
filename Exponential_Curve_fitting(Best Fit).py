import numpy as np

#Range
print("Enter a range")
n = int(input())

#Input x and calculate its sum
x = [float(input(np.array([i])))for i in range(n)]
sum_x=  sum(x)
print("x:",x)
print("sum_x:",sum_x)

#Input y and calculate its sum
y = [float(input(np.array([i])))for i in range(n)]
sum_y=  sum(y)
print("y:",y)
print("sum_y:",sum_y)

#Calculate Y = log y
Y = [np.log10(y[k])for k in range(n)]
sum_Y = sum(Y)
print("Y:",Y)
print("sum of Y:",sum_Y)


#Calculate square of x
x_2 = [x[k]**2 for k in range(n)]
sum_x_2 = sum(x_2)
print("Sqaure of x:",x_2)
print("Sum of sqaure of x:",sum_x_2)

#Calculate x multiply by y
x_Y = [x[k]*Y[k] for k in range(n)]
sum_x_Y = sum(x_Y)
print("x multiplied by y:",x_Y)
print("sum of x * y:",sum_x_Y)

#Equation 1
print("Equation 1:",sum_Y, "=", n,"A +",sum_x,"B" )

#Equation 2
print("Equation 2:",sum_x_Y, "=", sum_x,"A +",sum_x_2,"B" )

n_1 = sum_x /  n
sum_Y_1 = sum_Y * n_1
n_a = n * n_1
sum_x_1 = sum_x * n_1

print("Modified Equation:",sum_Y_1, "=", n_a,"A +",sum_x_1,"B" )

sub_a = sum_x_Y - sum_Y_1
sub_b = sum_x - n_a
sub_c = sum_x_2 - sum_x_1

print("After Subtration we get:",sub_a, "=",sub_b,"A +",sub_c,"B")

B = sub_a / sub_c
print("B = ", B)

print("Putting B's value in eqn(i) we get :")

A = (sum_Y-(sum_x * B))/n

print("A =" ,A)

print("We know A= log10(a) and B =log10(b) ")
print("Hence log10(a) =",A,"and log10(b)=",B )

#Antilog and round upto decimal 2

a = np.round((10**A),2)
b = np.round((10**B),2)

print("a=", a)
print("b=", b)

print("Therefore we get the equation: y =",a,"(",b,")^x")

y_final = [a*pow(b,x[k])for k in range(n)]

print("Best fit acquired in exponential curve , y =",y_final)

#plotting x and y
from matplotlib import pyplot as plt
plt.scatter(x,y,color='red')
plt.plot(x,y,color='violet')
plt.plot(x,y_final)
plt.title('Best Fit in a Exponential curve')
plt.show()
