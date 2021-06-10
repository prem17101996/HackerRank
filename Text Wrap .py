import textwrap

def wrap(string, max_width):
    
    lst3=[]
    for i in string:
        lst3.append(i)
   
    lst2=[]
    count=0
    re=len(string)%max_width
    re2=len(string)-re
    lst4=[]
    for i in range(int(len(lst3)/max_width)):
        lst=[]
        
        for j in range(max_width):
            lst.append(lst3[count])
            count+=1        
        
        str1=""
        for i in lst:
            str1=str1+i
        lst4.append(str1)
    for i in lst4:
        print(i)
    return(string[re2:])
     
    
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)