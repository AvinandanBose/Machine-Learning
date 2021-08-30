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

if (n%2 != 0) and ((x[1]-x[0]) == (x[3]-x[2])):
    s= x[1]-x[0]
    mean = np.mean(x)
    u = [(x[k] - mean)/s for k in range(n)]
    sum_u = sum(u)
elif(n%2 == 0) and ((x[1]-x[0]) == (x[3]-x[2])):
    s_1= 1/2 * (x[1]-x[0])
    two_med_val = [x[len(x)//2],x[len(x)//2-1]]
    mean_1 = np.mean(two_med_val)
    u = [(x[k] - mean_1)/s_1 for k in range(n)]
    sum_u = sum(u)
else:
    u = np.round([x[k] - np.mean(x)for k in range(n)])
    sum_u = sum(u)

sorted_u = np.sort(u) 
print("u:",sorted_u)
print("summation of u:", sum_u)

#Calculation of u**2
u_2 = np.square(sorted_u)
sum_u_2 = sum(u_2)
print("Square of u:", u_2)
print("Summation of square of u:", sum_u_2)


#Calculation of u*y and its sum
u_y = [sorted_u[k] * y[k] for k in range(n)]
sum_u_y = sum(u_y)
print("u_y:",u_y)
print("sum_u_y:",sum_u_y)

print ("Equation 1:",sum_y,"=",n,"a +",sum_u,"b")
print ("Equation 2:",sum_u_y,"=",sum_u,"a +",sum_u_2,"b")

if(sum_u == 1):
    sum_uy_f = sum_u_y * n
    sum_u_f = sum_u *n
    sum_u2_f = sum_u_2 * n
    print ("Modified Equation 2:",sum_uy_f,"=",sum_u_f,"a +",sum_u2_f,"b")
    sub_1 = sum_y - sum_uy_f
    sub_2 = n - sum_u_f
    sub_3 = sum_u_2 - sum_u2_f
    print("Equation stands after subtraction:",sub_1,"=",sub_2,"a +(",sub_3,")")
    b=sub_1/sub_3
    format_b = "{:.2f}".format(b) #String value
    format_b_1 = float(format_b ) #String value to float value
    print("formatted b(upto 2 decimal places)=",format_b_1)
    a = (sum_y + (sum_u*b))/n
    format_a = "{:.2f}".format(a) #String value
    format_a_1 = float(format_a ) #String value to float value
    print("formatted a(upto 2 decimal places)=",format_a_1)
    print("The final equation is (y=a+bu) : y=",format_a_1,"+(",format_b_1,")u")
    #Best fitted points of y corresponding to u values
    y_final = [format_a_1+format_b_1*u[k] for k in range(n)]
    print("Best fitted straight line y's point =",y_final)
    #plotting x and y
    from matplotlib import pyplot as plt
    plt.scatter(x,y)
    plt.plot(x,y_final)
    plt.title('Best Fit in a Straight Line')
    plt.show()
    
elif(sum_u == 0):
    b=sum_u_y/sum_u_2
    format_b = "{:.2f}".format(b) #String value
    format_b_1 = float(format_b ) #String value to float value
    print("formatted b(upto 2 decimal places)=",format_b_1)
    a=sum_y/n
    format_a = "{:.2f}".format(a) #String value
    format_a_1 = float(format_a ) #String value to float value
    print("formatted a(upto 2 decimal places)=",format_a_1)
    print("The final equation is (y=a+bu) : y=",format_a_1,"+(",format_b_1,")u")
    #Best fitted points of y corresponding to u values
    y_final = [format_a_1+format_b_1*u[k] for k in range(n)]
    print("Best fitted straight line y's point =",y_final)
    #plotting x and y
    from matplotlib import pyplot as plt
    plt.scatter(x,y)
    plt.plot(x,y_final)
    plt.title('Best Fit in a Straight Line')
    plt.show()
else:
    sum_y_f = sum_y * sum_u
    n_f = n * sum_u
    sum_uf = sum_u * sum_u
    print ("Modified Equation 1:",sum_y_f,"=",n_f,"a +",sum_uf,"b")
    sum_uy_f = sum_u_y * n
    sum_u_f = sum_u *n
    sum_u2_f = sum_u_2 * n
    print ("Modified Equation 2:",sum_uy_f,"=",sum_u_f,"a +",sum_u2_f,"b")
    sub_1 = sum_y_f - sum_uy_f
    sub_2 = n_f - sum_u_f
    sub_3 = sum_uf - sum_u2_f
    print("Equation stands after subtraction:",sub_1,"=",sub_2,"a +(",sub_3,")")
    b=sub_1/sub_3
    format_b = "{:.2f}".format(b) #String value
    format_b_1 = float(format_b ) #String value to float value
    print("formatted b(upto 2 decimal places)=",format_b_1)
    a = (sum_y + (sum_u*b))/n
    format_a = "{:.2f}".format(a) #String value
    format_a_1 = float(format_a ) #String value to float value
    print("formatted a(upto 2 decimal places)=",format_a_1)
    print("The final equation is (y=a+bu) : y=",format_a_1,"+(",format_b_1,")u")
    #Best fitted points of y corresponding to u values
    y_final = [format_a_1+format_b_1*u[k] for k in range(n)]
    print("Best fitted straight line y's point =",y_final)
    #plotting x and y
    from matplotlib import pyplot as plt
    plt.scatter(x,y)
    plt.plot(x,y_final)
    plt.title('Best Fit in a Straight Line')
    plt.show()

    

    

    
