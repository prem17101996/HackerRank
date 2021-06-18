#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    lst=[]
    for grade in grades:
        grade=int(grade)
        ave=grade//5
        mgrades=5*(ave+1)
        if grade<38:
            lst.append(grade)
        else:
            if (mgrades-grade)<3:
                lst.append(mgrades)
            else:
                lst.append(grade)
    return(lst)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
