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

#Calculation of x**2
x_2 = [x[k]**2 for k in range(n)] #np.square() function can be used
sum_x_2 = sum(x_2)
print("Square of x:",x_2)
print("Sum of square of x:",sum_x_2)

#Calculation of x**3
x_3 = [x[k]**3 for k in range(n)] 
sum_x_3 = sum(x_3)
print("Cube of x:",x_3)
print("Sum of cube of x:",sum_x_3)


#Calculation of x**4
x_4 = [x[k]**4 for k in range(n)] 
sum_x_4 = sum(x_4)
print("x power 4 :",x_4)
print("Sum of x power 4:",sum_x_4)


#Calculation of xy
x_y = [x[k] * y[k] for k in range(n)]
sum_x_y = sum(x_y)
print("x * y :",x_y)
print("Sum of x * y:",sum_x_y)

#Calculation of x**2*y
x_2_y = [x_2[k] * y[k] for k in range(n)]
sum_x_2_y = sum(x_2_y)
print("x ** 2 * y :",x_2_y)
print("Sum of x**2*y:",sum_x_2_y)

#Equation 1
print("Equation 1:",sum_y,"=",n,"a +",sum_x,"b +",sum_x_2,"c")

#Equation 2
print("Equation 2:",sum_x_y,"=",sum_x,"a +",sum_x_2,"b +",sum_x_3,"c")

#Equation 3
print("Equation 3:",sum_x_2_y,"=",sum_x_2,"a +",sum_x_3,"b +",sum_x_4,"c")


#Modified Equation 1
n_a = sum_x/n
sum_y_1 = sum_y * n_a
n_1 = n*n_a
sum_x_1 = sum_x * n_a
sum_x_2_1 = sum_x_2 *n_a
print("Modified Equation 1:",sum_y_1,"=",n_1,"a +",sum_x_1,"b +",sum_x_2_1,"c")

print("After subtracting Modified Equation 1 from Equation 2 we get:")
sub_1 = sum_x_y - sum_y_1
sub_2 = sum_x - n_1
sub_3 = sum_x_2 - sum_x_1
sub_4 = sum_x_3 - sum_x_2_1
print("Equation after Subtration (1):",sub_1,"=",sub_2,"a +",sub_3,"b +",sub_4,"c")

#Modified Equation 2
n_b = sum_x_2/n
sum_y_a = sum_y * n_b
n_2 = n * n_b
sum_x_a = sum_x * n_b
sum_x_2_a = sum_x_2 * n_b
print("Modified Equation 2:",sum_y_a,"=",n_2,"a +",sum_x_a,"b +",sum_x_2_a,"c")

print("After subtracting Modified Equation 2 from Equation 3 we get:")
sub_a = sum_x_2_y - sum_y_a
sub_b = sum_x_2 - n_2
sub_c = sum_x_3 - sum_x_a
sub_d = sum_x_4 - sum_x_2_a
print("Equation after Subtration (2):",sub_a,"=",sub_b,"a +",sub_c,"b +",sub_d,"c")

div_new = sub_c/sub_3
sub_new_a = sub_1 * div_new
sub_new_b = sub_2 * div_new
sub_new_c = sub_3 * div_new
sub_new_d = sub_4 * div_new
print("Modified Equation 3:",sub_new_a,"=",sub_new_b,"a +",sub_new_c,"b +",sub_new_d,"c")

print("After subtracting Modified Equation 3  we get:")

subtract_1= sub_a - sub_new_a 
subtract_2= sub_b - sub_new_b 
subtract_3= sub_c - sub_new_c
subtract_4= sub_d - sub_new_d
print(" Equation 4:",subtract_1,"=",subtract_2,"a +",subtract_3,"b +",subtract_4,"c")


c = subtract_1 / subtract_4
b = (sub_1 - (sub_4 * c))/sub_3
a = (sum_y - (sum_x *b + sum_x_2*c))/n

print("a=",a)
print("b=",b)
print("c=",c)

print("y = a + bx + cx^2 =>",a,"+",b,"x+",c,"x^2")

y_final = [a + b*x[k] + c*x_2[k] for k in range(n)]
print("Best fit acquired in parabolic curve , y =",y_final)
      
#plotting x and y
from matplotlib import pyplot as plt
plt.scatter(x,y)
plt.plot(x,y_final)
plt.title('Best Fit in a Parabolic curve')
plt.show()
