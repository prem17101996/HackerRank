t=int(input())
lst=[]
result=[]
for i in range(t):
    name=list(map(str,input().split()))
    result.append(name[0])
    name.pop(0)
    total=0
    for i in name:
        total=total+float(i)

    avg=float(total/len(name))
    result.append(avg)
    name=[]

Find_avg=input()
for i in range(len(result)):
    if result[i]==Find_avg:
        print("%.2f" %result[i+1])
