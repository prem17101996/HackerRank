#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    lst2=[]
    lst2.append(len(arr))
    for j in range(max(arr)):
        lst=[]
        for i in arr:
            
            if i-min(arr)!=0:
                lst.append(i-min(arr))
        lst2.append(len(lst))
        arr=lst
        if len(arr)==0:
            break
        lst=[]

    lst2.remove(lst2[-1])
    return lst2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
