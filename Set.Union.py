
n=int(input())
nnum=set(map(int,(input().split()[:n])))
b=int(input())
bnum=set(map(int,(input().split()[:b])))
u_num=nnum.union(bnum)
print(len(list(u_num)))
