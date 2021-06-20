#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    ar=list(set(arr))
    lst=[]
    for i in ar:
        lst.append(arr.count(i))
        
    max_lst=max(lst)
    lst1=[]
    for i in range(len(ar)):
        lst1.append(ar[i])
        lst1.append(lst[i])
    lst2=[]
    for i in range(len(lst1)):
        if i%2==1:
            if max_lst==lst1[i]:
                lst2.append(lst1[i-1])
    return(min(lst2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
