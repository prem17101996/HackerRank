from itertools import permutations
s,n=input().split()

lst=list(permutations(s,int(n)))
lst.sort()
str1=""
for i in lst:
    str1=""
    for j in range(int(n)):
        str1=str1+str(i[j])
    print(str1)