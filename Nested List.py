if __name__ == '__main__':
    lst=[]
    lst2=[]


for _ in range(int(input())):
    name=input("")
    score=float(input(""))
    lst1=[]
    lst1.append(name)
    lst1.append(score)
    lst.extend(lst1)
    lst2.append(score)
    lst2.sort()
if lst2[0]!=lst2[1]:
    lst3=[]
    for i in range(len(lst)):
        if lst[i] == lst2[1]:
            lst3.append(lst[i- 1])
    lst3.sort()
    for i in lst3:
        print(i)

if(lst2[0]==lst2[2]):

    lst4=[]

    for i in range(len(lst)):

        if lst[i] == lst2[3]:

            lst4.append(lst[i-1])


    lst4.sort()
    
    for i in lst4:
        print(i)
if (lst2[0] == lst2[1] and lst2[0] != lst2[2]):
    lst5=[]
    for i in range(len(lst)):
        if lst[i] == lst2[2]:

            lst5.append(lst[i-1])



    lst5.sort()
    for i in lst5:
        print(i)

 
v