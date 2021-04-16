import numpy
n,m=map(int,(input().split()))
lst=[]
for i in range(n):
    num=list(map(int,(input().split()[:m])))
    lst.append(num)

for i in range(4):
    if len(lst)==1:
        my_array = numpy.array([lst[i]])
        print (numpy.transpose(my_array))
        print (my_array.flatten())
        break
    elif len(lst)==2:
        my_array = numpy.array([lst[i],
                        lst[i+1]])
        print (numpy.transpose(my_array))
        print (my_array.flatten())
        break
    elif len(lst)==3:
        my_array = numpy.array([lst[i],
                        lst[i+1],lst[i+2]])
        print (numpy.transpose(my_array))
        print (my_array.flatten())
        break
    elif len(lst)==4:
        my_array = numpy.array([lst[i],lst[i+1],lst[i+2],lst[i+3]])
        print (numpy.transpose(my_array))
        print (my_array.flatten())
        break
        
    


