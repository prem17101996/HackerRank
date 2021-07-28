#!/bin/python3

import math
import os
import random
import re
import sys



def superDigit(n, k):
    n=str(n)
    lst=[]
    
    for i in n:
        lst.append(int(i)) 
    n1=str(sum(lst)*k )
    # print(n1)
    lst=[]
    for j in range (len(n)):
        
        for i in range(len(n1)):
            
            lst.append(int(n1[i]))
        # print(lst)
        if len(lst)==1:
            return(lst[0])
            break
        n1=sum(lst)
        n1=str(n1)
        lst=[]
       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
