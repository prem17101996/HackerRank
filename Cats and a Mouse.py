#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    print(x,y,z)
    sum1=z-x
    sum2=z-y
    if sum1<0:
        sum1=-sum1
    else:
        sum1=sum1
    if sum2<0:
        sum2=-sum2
    else:
        sum2=sum2
    if sum1==sum2:
        return("Mouse C")
    elif sum1>sum2:
        print(sum1,sum2)
        return("Cat B")
    else:
        return("Cat A")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
