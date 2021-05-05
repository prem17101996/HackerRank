
from itertools import combinations
name,k=map(str,(input().split()))

lst2=[]
for i in name:
    lst2.append(i)
lst2.sort()
str1=""
lst3=[]
for i in lst2:
    str1=str1+i

for i in range(1,int(k)+1):
    lst=list(combinations(str1,int(i)))
    lst3.extend(lst)

for i in lst3:
    str2=""
    for j in range(len(i)):
        str2=str2+i[j]
    print(str2)

