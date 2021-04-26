#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    lst=[]
    lst2=[]
    lst3=[]
    for i in s:
        lst.append(i)
    lst.sort()
    # print(lst)
    lst1=set(lst)   
    lst1=list(lst1)
    lst1.sort()
    # print(lst1)
    for i in range(len(lst1)):
        cou=lst.count(lst1[i])
        lst2.append(cou)
    # print(lst2)
    for i in range(len(lst2)):
        lst3.append(lst1[i])
        lst3.append(lst2[i])
    # print(lst3)
    lst2.sort()
    # print(lst2)
    for i in range(len(lst3)):
        if lst2[-1]==lst3[i]:
            print(lst3[i-1]+ " "+str(lst2[-1]))
            break
    lst3.remove(lst2[-1])
            
    # print(lst3)
    for i in range(len(lst3)-1):
        if lst2[-2]==lst3[i]:
            print(lst3[i-1]+ " "+str(lst2[-2]))
            break
    lst3.remove(lst2[-2])
    # print(lst3)         
    for i in range(len(lst3)-1):
        if lst2[-3]==lst3[i]:
            print(lst3[i-1]+ " "+str(lst2[-3]))
            break 
    