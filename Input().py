# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=list(map(int,(input().split())))
equation=input()
new_equation=equation.replace('x','a')
result=eval(new_equation) 
if result==b:
    print("True")
else:
    print("False")

