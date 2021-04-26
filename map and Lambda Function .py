 # complete the lambda function 
cube=lambda x:x**3
def fibonacci(n):
    lst=[0,1]
    lst1=[0]
    lst3=[]    
    for i in range(n-2):
        
        sum=lst[-2]+lst[-1]
        lst.append(sum)
    
    if n==1 :
        return lst1
    elif n==0:
        return lst3
    
    else:
        return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))