#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    lst1=[]
    lst2=[]
    for i in s1:
        lst1.append(i)
    for i in s2:
        lst2.append(i)
    # print(lst1,lst2)
    lst1=list(set(lst1))
    lst2=list(set(lst2))
    
    for i in lst1:
        if i in lst2:
            return("YES")
            break
    else:
        return("NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
