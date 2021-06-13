t=input()
num=(input().split())
num.sort() 
if int(num[0])>=1:
    for i in num:       
        if (i)==i[::-1]:           
            print("True")
            break
    else:
        print("False")
        
            
else:
    print("False")
