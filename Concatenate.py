import numpy

n,m,p=list(map(int,(input().split())))
lst=[]
for i in range(n+m):
    num=list(map(int,(input().split())))
    lst.append(num)
    

my_array = numpy.array(lst)
print(my_array)



