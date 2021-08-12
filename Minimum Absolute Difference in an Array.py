#!/bin/python3

import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    count=0
    lst=[]
    ra=0
    for i in range(len(arr)-1):
        count=i+1
        ra=ra+1
        for j in range(len(arr)-ra):
            lst.append(abs(arr[i]-arr[count]))
            count+=1
        
    return(min(lst))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
