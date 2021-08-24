#Using List comprehension in a single line approach
import numpy as np
print("Enter a range")

#list comprehension in one line :)
n = range(int(input()))
x = [float(input(np.array([i])))for i in n]
sum_1=  sum(x) #sum function
print(x)
print(sum_1)

#User Input in Two Dimensional Array in Numpy
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = np.zeros((m,n),dtype=int)
u = len(a)
print('a=',a)
print('length of a i.e. u =',u)
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter an element:"))
        a[i][j]=x


for i in range(u):
    for j in range(len(a[i])):
       print(a[i][j])

print(a)

#User input in array
import array as arr #from array import *
m = int(input("Enter the length of the array: "))
arr_1 = arr.array('i',[]) #i->integer
for i in range(m):
    arr_1.append(int(input("Enter the value:")))
print(arr_1)


#Using list for two dimensional array approach
m = int(input("Enter number of Row:"))
n = int(input("Enter number of Column:"))
Mat = []
for i in range (0,m):
    Mat.append([])
print("Blank columns of MAT:",Mat)
for i in range (0,m):
    for j in range(0,n):
        Mat[i].append(j)
        Mat[i][j]=0
print("Zeroes filled in list:",Mat)
for i in range (0,m):
    for j in range(0,n):
        print('entry in row:', i+1,
              'column:' , j+1)
        Mat[i][j] = int(input())
print(Mat)


#Using list for two dimensional array approach - Type 2
m = int(input("Enter number of Row:"))
n = int(input("Enter number of Column:"))
Mat = []
for i in range (0,m):
    Mat.append([])
print("Blank columns of MAT:",Mat)
for i in range (0,m):
    for j in range(0,n):
        Mat[i].append(j)
        Mat[i][j]=0
print("Zeroes filled in list:",Mat)

u = len(Mat)
print('length of mat:',u)
for i in range(u):
    for j in range(len(Mat[i])):
        x = int(input("Enter an element:"))
        Mat[i][j]=x
print(Mat)

