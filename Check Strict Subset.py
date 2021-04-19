a=list(map(int,(input().split())))
t=int(input())
lst=[]
for i in range(t):
    n=list(map(int,(input().split())))
    for i in n:
        lst.append(i)
for i in range(len(lst)):
    if lst[i] not in a:
        print("False")
        break
else:
    print("True")
