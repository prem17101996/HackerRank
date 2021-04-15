# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
nnum=set(map(int,(input().split()[:n])))
b=int(input())
bnum=set(map(int,(input().split()[:b])))
intersect_num=nnum.intersection(bnum)
print(len(list(intersect_num)))
