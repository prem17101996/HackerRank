
s=input()
k=input()

lst1=[]
lst=[]

for i in s:
    if k in s:
        ind=s.index(k)
        lst.append(ind)
        lst.append(ind+len(k)-1)
        lst=tuple(lst)
        
        lst1.append(lst)
        s=s.replace(i," ",1)
        
        
        lst=[]

lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
if len(lst2)>0:
    for i in lst2:
        print(i)
else:
    print("(-1, -1)")        


