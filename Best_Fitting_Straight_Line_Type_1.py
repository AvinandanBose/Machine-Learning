import numpy as np

#Range
print("Enter a range")
n = int(input())

#Input x and calculate its sum
x = [int(input(np.array([i])))for i in range(n)]
sum_x=  sum(x)
print("x:",x)
print("sum_x:",sum_x)

#Input y and calculate its sum
y = [int(input(np.array([i])))for i in range(n)]
sum_y=  sum(y)
print("y:",y)
print("sum_y:",sum_y)

#Calculation of X**2
x_2 = np.square(x)
sum_x_2 = sum(x_2)
print("x_2:",x_2)
print("sum_x_2:",sum_x_2)


#Calculation of XY
x_y = [x[k] * y[k] for k in range(n)]
sum_x_y = sum(x_y)
print("x_y:",x_y)
print("sum_x_y:",sum_x_y)

print ("Equation 1:",sum_y,"=",n,"a +",sum_x,"b")
print ("Equation 2:",sum_x_y,"=",sum_x,"a +",sum_x_2,"b")
sum_y_2 = sum_y*sum_x
n_1 = n * sum_x
sum_x_3 = sum_x * sum_x
print ("Modified Equation 1:",sum_y_2,"=",n_1,"a +",sum_x_3,"b")

sum_x_y_1 = sum_x_y * n
sum_x_4 = sum_x * n
sum_x_2_1 = sum_x_2 * n
print (" Modified Equation 2:",sum_x_y_1,"=",sum_x_4,"a +",sum_x_2_1,"b")

print("Substracting Modified Equation 2 with Modified Equation 1 we get")
res_1 = sum_y_2 - sum_x_y_1
res_2 = n_1 - sum_x_4
res_3 = sum_x_3 - sum_x_2_1
print (" Final Equation after Subtsraction:",res_1,"=",res_2,"a +(",res_3,"b)")

b = res_1 / res_3

print("We get value of b=",b)

format_b = "{:.2f}".format(b) #String value
format_b_1 = float(format_b ) #String value to float value

print("formatted b(upto 2 decimal places)=",format_b_1)

print("putting b's value in Equation 1 : we get ")
a = (sum_y - (sum_x*format_b_1))/n
print("Value of a =",a)

format_a = "{:.2f}".format(a) #String value
format_a_1 = float(format_a ) #String value to float value

print("formatted a(upto 2 decimal places)=",format_a_1)

# y's equation we get:

print("y=a+bx => y =",format_a_1,"+",format_b_1,"x")


#Best fitted points of y corresponding to x values

y_final = [format_a_1+format_b_1*x[k] for k in range(n)]
print("Best fitted straight line y's point =",y_final)

#plotting x and y

from matplotlib import pyplot as plt
plt.scatter(x,y)
plt.plot(x,y_final)
plt.title('Best Fit in a Straight Line')
plt.show()
