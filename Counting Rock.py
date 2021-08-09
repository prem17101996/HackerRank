n,t=input().split()
num=list(map(int,(input().split())))
lst = []
str1=""
for i in range(int(t)):

    add=0
    range1,range2=input().split()

    for j in num:
        if int(range1)<j<int(range2):
            # print(j)
            add+=1
    lst.append(add)
for i in lst:
    str1=str1+str(i)+" "
print(str1)
