# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    a=int(input())
    n1=list(map(int,(input().split()[:a])))
    b=int(input())
    n2=list(map(int,(input().split()[:b])))
    for i in range(len(n1)):
        if n1[i] not in n2:
            print("False")
            break
    else:
        print("True")
            
