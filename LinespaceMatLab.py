import numpy as np

#LinSpace(startpoint , endpoint)
numbers = np.linspace(0,10)
print(type(numbers))
print(numbers)


#LinSpace(startpoint , endpoint, numberofSamples)
numbers1 = np.linspace(start=0,stop=10,num=25)
print(type(numbers1))
print(numbers1)

#LinSpace(startpoint , endpoint, numberofSamples, endpoint(when False))
numbers2 = np.linspace(start=0,stop=10,num=25,endpoint=False)
print(type(numbers2))
print(numbers2)

#LinSpace(startpoint , endpoint, numberofSamples, endpoint(when False),retstep)
numbers3 = np.linspace(start=0,stop=10,num=25,endpoint=False,retstep=True)
print(type(numbers3))
print(numbers3)
