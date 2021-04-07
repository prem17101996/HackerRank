# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
lst=[]
for i in range(n):
    country=input()  
    lst.append(country)
lst=set(lst)
lst=list(lst)
print(len(lst))
