import numpy
n=input()
lst=[]
for i in range(int(n)):
    num=list(map(float,(input().split())))
    lst.append(num)
 
print (round(numpy.linalg.det(lst),2))

