n,k=input().split()
num=list(map(int,(input().split())))

for i in range(int(k)):
    j=num.index(max(num))
    z=max(num)//2
    num.remove(max(num))
    num.insert(j,z)
print(sum(num))