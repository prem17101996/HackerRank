import numpy
n,m=(input().split())
lst=[]
for i in range(int(n)):
    num1=list(map(int,(input().split())))
    lst.append(list(num1))
 
my_array = numpy.array(lst)
min_value=numpy.min(my_array, axis = 1)

print(max(min_value))


