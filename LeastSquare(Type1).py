import numpy as np
from matplotlib import pyplot as plt
print("Enter a range")
n = int(input())
#list comprehension method
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0

#Enter values of x and calculating their sum(Summation)
print("Enter values of x and calculating their sum")
for i in range(n):
    x = float(input(np.array([i])))
    list_1.append(x)
    sum_1 = sum_1 + x
print(list_1)
print(sum_1)

#Enter values of (observed)y and calculating their sum(Summation)
print("Enter values of (observed) y and calculating their sum")
for j in range(n):
    y = float(input(np.array([j])))
    list_2.append(y)
    sum_2 = sum_2 + y
print(list_2)
print(sum_2)

#Estimated y and calculating their sum(Summation)
print("Estimated y and calculating their sum")
print("a:")
a = float(input())
print("b:")
b = float(input())       
for k in range(n):
    y_1 = a+b*list_1[k]
    list_3.append(y_1)
    sum_3 = sum_3 + y_1
print(list_3)
print(sum_3)


#Difference between observed y - estimated y
print("Difference between observed y - estimated y")
for l in range(n):
    y_2 = list_2[l] - list_3[l]
    list_4.append(y_2)
    sum_4 = sum_4 + y_2
print(list_4)
print(sum_4)


#Difference **2
print("Difference **2")
for m in range(n):
    y_3 = list_4[m]**2
    list_5.append(y_3)
    sum_5 = sum_5 + y_3
print(list_5)
print(sum_5)

from sklearn.model_selection import train_test_split
list_1_train,list_1_test,list_5_train,list_5_test = train_test_split(list_1,list_5,train_size=0.5,test_size=1/3,
                                                                     random_state=0)

#Printing the Training set
print("Printing the Training set")
print("x coordinates:",list_1_train)
print("y coordinates:",list_5_train)

#Visualizing the Training set result 
plt.scatter(list_1_train,list_5_train,color='blue')
plt.plot(list_1,list_5,color='red')
plt.title('Visualizing the Train set')
plt.xlabel('X Train')
plt.ylabel('Y Train')
plt.show()


#Printing the Test set
print("Printing the Test set")
print("x coordinates:",list_1_test)
print("y coordinates:",list_5_test)

#Visualizing the Test set result 
plt.scatter(list_1_test,list_5_test,color='blue')
plt.plot(list_1,list_5,color='red')
plt.title('Visualizing the Test set')
plt.xlabel('X Test')
plt.ylabel('Y Test')
plt.show()



