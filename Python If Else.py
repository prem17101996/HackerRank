#!/bin/python3

import math
import os
import random
import re
import sys



n=int(input())
if (n%2==1):
    print("Weird")
else:
    if (n==2 or n==4):
        print("Not Weird")

    elif(n==6 or n==8 or n==10 or n==12 or n==14 or n==16 or n==18 or n==20 ):
        print("Weird")

    elif(n>20):
        print("Not Weird")