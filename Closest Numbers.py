#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    lst=[]
    lst3=[]
    lst2=[]
    
    arr.sort()
    # print(arr,arr1)
    for i in range(len(arr)-1):
        sub=arr[i]-arr[i+1]
        if sub>=0:
            lst.append(sub)
        else:
            lst.append(-(sub))
    # print(arr)
    # print(lst)
    for i in lst:
        lst2.append(i)
    lst.sort()
    # print(lst,lst2)
    for i in range(len(lst2)):
        if lst2[i]==lst[0]:
           
            lst3.append(arr[i])
            lst3.append(arr[i+1])
    return(lst3)
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
