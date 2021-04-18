n=int(input())
lst=[]
for i in range(n):
    num=input()
    lst.append(num)

lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)


str1=""
for i in range(len(lst2)):
    count1=lst.count(lst2[i])
    str1=str1+str(count1)+" "
print(int(len(str1)/2))   
print(str1) 