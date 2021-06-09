#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=len(s)
    str1=""
    str2=""
    lst=[]
    for i in range(len(s)):
        if s[i]==" ":
            lst.append(i)
    s=s.split()
    
    for i in s:
        cap=i.capitalize()
        str1=str1+str(cap)
    # print(lst)
    # print(str1)
    coun=0
    for i in range(l):
        
        if i in lst:
            str2=str2+" "
        else:
            str2=str2+str(str1[coun])
            coun+=1
            
        
    return str2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
