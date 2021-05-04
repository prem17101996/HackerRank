# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
name,k=map(str,(input().split()))

lst2=[]
for i in name:
    lst2.append(i)
lst2.sort()
str1=""
for i in lst2:
    str1=str1+i
lst=list(combinations_with_replacement(str1,int(k)))

lst.sort()
for i in lst:
    str2=""
    for j in range(len(i)):
        str2=str2+i[j]
    print(str2)
