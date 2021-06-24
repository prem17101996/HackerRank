#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    lst=[]
    if n%2==0:
        n=n+1
    for i in range(1,n+1):
        if i%2==1:
            lst.append(i)
    lst1=lst[::-1]
    
    count=0
    for i in lst:
        count+=1
        if p<=i:
            break
    coun=0
    for i in lst1:
        coun+=1
        
        if p==i or p==i-1:
             
            break
    count-=1
    coun-=1       
    if count<=coun:
        return(count)
    else:
        return(coun)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
