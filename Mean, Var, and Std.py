# import numpy
import numpy
n,m=(input().split())
lst=[]
for i in range(int(n)):
    num1=list(map(int,(input().split())))
    lst.append(num1)

my_array = numpy.array(lst)
mean_value=numpy.mean(my_array, axis = 1)
var_value=numpy.var(my_array, axis = 0)
std_value=numpy.std(my_array)
print(mean_value)
print(var_value)
numpy.set_printoptions(legacy='1.13')

print(std_value)

 






