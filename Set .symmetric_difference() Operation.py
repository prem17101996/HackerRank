# Enter your code here. Read input from STDIN. Print output to STDOUT
t1=int(input())
n1=list(map(int,input().split()[:t1]))
t2=int(input())
n2=list(map(int,input().split()[:t2]))
lst1=[]
lst2=[]
for i in range(len(n1)):
    
    if n1[i] not in n2:
       lst1.append(n1[i]) 
       
for i in range(len(n2)):
    
    if n2[i] not in n1:
       lst2.append(n2[i])
print(len(lst1)+len(lst2)) 
       
