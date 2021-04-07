# Enter your code here. Read input from STDIN. Print output to STDOUT
t1=int(input())

a=list(map(int,(input().split()[:t1])))
t2=int(input())
b=list(map(int,(input().split()[:t2])))

a=set(a)
b=set(b)
un=a.union(b)
inter=a.intersection(b)

symetric=un-inter
symetric=list(symetric)
symetric.sort()

for i in symetric:
    print(i)
