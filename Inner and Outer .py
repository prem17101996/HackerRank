import numpy

a= list(map(int,(input().split())))
b= list(map(int,(input().split())))
A = numpy.array(b)
B = numpy.array(a)

print (numpy.inner(A, B))
C = numpy.array(a)
D= numpy.array(b)

print (numpy.outer(C, D))

