#!/bin/python3

import os
import sys
def timeConversion(s):

    if s[-2]=='P' :
        if s[0:2]=="12":
            sum=str(int(s[0:2]))
        else:
            sum=str(12+int(s[0:2]))
            
        
        
        s1=s.replace(s[:2],sum)
        s2=s1.replace('P','')
        s3=s2.replace('M','')
        return s3
    
    else:
        if s[0:2]=="12":
            s=s.replace(s[0:2],"00")
            
      
        s1=s.replace('A','')
        s2=s1.replace('M','')
        return s2
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
