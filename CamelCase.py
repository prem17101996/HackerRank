#!/bin/python3

import math
import os
import random
import re
import sys


def camelcase(s):
    for i in s:
        if i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="O" or i=="P" or i=="Q" or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="W" or i=="X" or i=="Y" or i=="Z":
            s=s.replace(i,",")
    
    return(s.count(",")+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
