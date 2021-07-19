#!/bin/python3

import math
import os
import random
import re
import sys


def stringConstruction(s):
    lst=[]
    for i in s:
        lst.append(i)
    lst=list(set(lst))
    return(len(lst))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
