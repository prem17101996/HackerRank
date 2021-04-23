k=int(input())
num=list(map(int,(input().split())))
num_s=set(num)
print(((sum(num_s)*k)-sum(num))//(k-1))