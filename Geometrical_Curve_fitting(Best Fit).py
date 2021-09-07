import numpy as np

#Range
print("Enter a range")
n = int(input())

#Input x 
x = [float(input(np.array([i])))for i in range(n)]
print("x:",x)

#Input y
y = [float(input(np.array([i])))for i in range(n)]
print("y:",y)

#X=log(x)
X = [np.log10(x[k])for k in range(n)]
print("X:",X)

#Rounded X=log(x) and its sum
round_X = np.round([X[k]for k in range(n)],2)
sum_round_X = np.round(sum(round_X),2)
print("Rounded X upto 2 decimal places:",round_X)
print("Sum of round X:",sum_round_X)

#Y=log(y)
Y = [np.log10(y[k])for k in range(n)]
print("Y:",Y)


#Rounded Y=log(y)
round_Y = np.round([Y[k]for k in range(n)],2)
sum_round_Y = np.round(sum(round_Y),2)
print("Rounded Y upto 2 decimal places:",round_Y)
print("Sum of round Y:",sum_round_Y)

print("Putting these values we get equations:")
print("Eqn 1:",sum_round_Y,)

#Square of X (Rounded)
square_round_X =[round_X[k]**2 for k in range(n)]
sum_of_square_round_X  = sum(square_round_X)
print("Square of X:",square_round_X)
print("Sum of Square of X:",sum_of_square_round_X)


#X*Y
X_Y = [round_X[k]*round_Y[k] for k in range(n)]
sum_X_Y = sum(X_Y)
print("X * Y:",X_Y)
print("Sum of X * Y:",sum_X_Y)

print("Putting these values we get equations:")
print("Eqn 1:",sum_round_Y,"=",n,"A +",sum_round_X,"n")
print("Eqn 2:",sum_X_Y,"=",sum_round_X,"A +",sum_of_square_round_X,"n")

print("Dividing Eqn 1 with ",n, "we get:" )
div_1 = sum_round_Y/n
div_2 = n/n
div_3 = sum_round_X / n

print("Modified Eqn 1:",div_1,"=",div_2,"A +",div_3,"n")

print("Dividing Eqn 2 with ",sum_round_X, "we get:" )

div_a = sum_X_Y/sum_round_X
div_b = sum_round_X / sum_round_X
div_c = sum_of_square_round_X/ sum_round_X

print("Modified Eqn 2:",div_a,"=",div_b,"A +",div_c,"n")

print("Subtracting Modified Eqn 2 from Modified Eqn 1 we get")

sub_1 = div_1 - div_a
sub_2 = div_2 - div_b
sub_3 = div_3 - div_c

print("Final Eqn :",sub_1,"=",sub_2,"A +",sub_3,"n")

N = np.round(sub_1/sub_3,1)
A = div_1-(div_3 *N)

print("N:",N)
print("A:",A)
print("We know A= log a, hence log a =",A )

#calculation of antilog

a = np.round(pow(10,A),1)

print("a=",a)

print(" Therefore y =",a,"x^",N)

y_final = [a*(pow(x[k],N))for k in range(n)]

print("Best fit acquired in geometrical curve , y =",y_final)

#plotting x and y
from matplotlib import pyplot as plt
plt.scatter(x,y,color='red')
plt.plot(x,y,color='violet')
plt.plot(x,y_final)
plt.title('Best Fit in a Geometric curve')
plt.show()
