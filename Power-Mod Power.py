# Enter your code here. Read input from STDIN. Print output to STDOUT
a=float(input())
b=float(input())
m=float(input())
lst=[]
powe=a**b
mod=powe%m
lst.append(powe)
lst.append(mod)
for i in lst:
    print(int(i))
