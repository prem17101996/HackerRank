import math
t1=int(input())
n1=list(map(int,(input().split()[:t1])))
t2=int(input())
n2=list(map(int,(input().split()[:t2])))
lst=[]
for i in range(len(n1)):
    if n1[i] not in n2:
        lst.append(n1[i])
print(len(lst))