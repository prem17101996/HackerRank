# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    num=input()
    cou=num.count(".")
    
    
    if "." in num:
        if (num[0]=="-" or num[0]=="+" or num[0]=="."or num[0]=="1"or num[0]=="2"or num[0]=="3"or num[0]=="4"or num[0]=="5"or num[0]=="6"or num[0]=="7"or num[0]=="8"or num[0]=="9"or num[0]=="0" ):
            
            if num[-1]!="." and cou==1:
                
                for j in num[1:]:
                    
                    if j=="+" or j=="-" or j=='A' or j=='B' or j=='C' or j=='D'  or j=='E' or j=='F' or j=='G' or j=='H' or j=='I' or j=='J' or j=='K' or j=='L' or j=='M' or j=='N' or j=='O' or j=='P' or j=='Q' or j=='R' or j=='S' or j=='T' or j=='U' or j=='V' or j=='W' or j=='X' or j=='Y' or j=='Z' or j=='a' or j=='b' or j=='c' or j=='d'  or j=='e' or j=='f' or j=='g' or j=='h' or j=='i' or j=='j' or j=='k' or j=='l' or j=='m' or j=='n' or j=='o' or j=='p' or j=='q' or j=='s' or j=='r' or j=='t' or j=='u' or j=='v' or j=='w' or j=='x' or j=='y' or j=='z':
                        print("False")
                        break
                else:
                    print("True")
                    
            else:
                print("False")
                
        else:
            print("False")            
    else:
        print("False")
