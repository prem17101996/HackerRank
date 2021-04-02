n=int(input())
lst=[]
a = list(map(int, input("").split()))
for i in a:
    lst.append(i)
lst=set(lst)
lst=list(lst)
lst.sort()

print(lst[-2])
