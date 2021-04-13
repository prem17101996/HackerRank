# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
lst=[]
for i in range(t):
    n=list(map(str,(input().split())))
    if n[0]=="append":
        lst.append(int(n[1]))
    elif n[0]=="appendleft":
        lst.insert(0,int(n[1]))
    elif n[0]=="pop":
        lst.pop()
    elif n[0]=="popleft":
        lst.pop(0)

str1=""
for i in lst:
    str1=str1+str(i)+" "
print(str1)   
     
    
