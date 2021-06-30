#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    lst=[]
    for p in range(i,j+1):
        p=str(p)
        lst.append((int(p)-int(p[::-1]))/k)
    count=0
    for i in lst:
        if i%2==0:
            count+=1 
        elif i%2==1:
            count+=1
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
