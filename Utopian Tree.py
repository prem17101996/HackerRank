#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    
    lst=[]
    for i in range(n+1):
        if i==0:
            lst.append("1")
        elif i%2==1:
            mul=int(lst[-1])*2
            lst.append(mul)
            mul=1
        else:
            
            sum1=int(lst[-1])+1
            lst.append(sum1)
    
    return(lst[n])
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
