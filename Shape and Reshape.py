import numpy
num=list(map(int,(input().split())))

my_array = numpy.array(num)
print (numpy.reshape(my_array,(3,3)))
