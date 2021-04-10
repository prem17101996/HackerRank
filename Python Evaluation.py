# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
t=list(t)
t.remove("p")
t.remove("r")
t.remove("i")
t.remove("n")
t.remove("t")

s="".join(t)
print(eval(s))

    
