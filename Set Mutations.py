# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
n=set(map(int,(input().split()[:a])))
t=int(input())

for i in range(t):
    b=list(map(str,(input().split())))
    n1=set(map(int,(input().split())))  
    if b[0]=='intersection_update':
        n.intersection_update(n1)

    elif b[0]=='update':
        n.update(n1)

    elif b[0]=='symmetric_difference_update':
        n.symmetric_difference_update(n1) 
 
    elif b[0]=='difference_update':
        n.difference_update(n1) 
        
n=list(n)
print(sum(n))   

