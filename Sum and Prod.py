import numpy
n,m=(input().split())
lst=[]
for i in range(int(n)):
    num1=list(map(int,(input().split())))
    lst.append(list(num1))
    
my_array = numpy.array(lst)
n=numpy.sum(my_array, axis = 0)
prod=1
for i in n:
    prod=prod*int(i)
print(prod) 

