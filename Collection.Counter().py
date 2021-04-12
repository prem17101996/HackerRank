# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
xnum=list(map(int,(input().split()[:x])))
n=int(input())
lst=[]
for i in range(n):
    x,y=map(int,(input().split()))
    for j in range(len(xnum)):
        if xnum[j]==x:
            xnum.remove(xnum[j])
            lst.append(y)
            break
print(sum(lst))