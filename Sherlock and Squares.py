#!/bin/python3

import math
import os
import random
import re
import sys


def squares(a, b):
    
    num1=(math.sqrt(a))
    num2=math.sqrt(b)
    if num1%2==1 or num1%2==0:
        num1=int(num1)-1
    return(int(num2)-int(num1))
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
