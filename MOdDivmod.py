a=int(input())
b=int(input())
print(a//b)
print(a%b)
lst=[]
lst.append(a//b)
lst.append(a%b)
print(tuple(lst))