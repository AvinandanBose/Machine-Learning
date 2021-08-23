import numpy as np
from matplotlib import pyplot as plt
a = float(input("Enter a ="))
b = float(input("Enter b = "))
c = float(input("Enter c ="))
x= list(np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]))
y=[(a+b*i+c*i**2) for i in x]

#Splitting the data set into the Training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.5,test_size = 1/3,random_state=0)

#Visualizing the Training set result 
plt.scatter(x_train,y_train,color='blue')
plt.plot(x,y,color='red')
plt.title('Visualizing the Train set')
plt.xlabel('X Train')
plt.ylabel('Y Train')
plt.show()

#Visualizing the Training set result
plt.scatter(x_test,y_test,color='blue')
plt.plot(x,y,color='red')
plt.title('Visualizing the Test set')
plt.xlabel('X Test')
plt.ylabel('Y Test')
plt.show()
