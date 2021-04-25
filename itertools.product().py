from itertools import product
a=map(int,(input().split()))
b=map(int,(input().split()))
lst=list(product(a,b))
for i in lst:
    print(i,end=" ") 