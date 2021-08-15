#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    result=str(bin(n))
    result=result.replace(result[0:2],"")
    res=(32-len(result))*"0"
    # print(res)
    result=res+result
    
    result=result.replace("0","2")
    result=result.replace("1","0")
    result=result.replace("2","1")
    final_result=int(result,2)
    return(final_result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
