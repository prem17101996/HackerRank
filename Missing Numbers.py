#!/bin/python3

import math
import os
import random
import re
import sys


def missingNumbers(arr, brr):
    for i in arr:
        brr.remove(i)
    brr=list(set(brr))
    brr.sort()
    
    return(brr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
