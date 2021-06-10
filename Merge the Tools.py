def merge_the_tools(string, k):
    lst3=[]
    for i in string:
        lst3.append(i)
   
    lst2=[]
    count=0
    for i in range(int(len(lst3)/k)):
        lst=[]
        lst4=[]
        for j in range(k):
            lst.append(lst3[count])
            count+=1        
        for j in lst:
            if j not in lst4:
                lst4.append(j)
        str1=""
        for i in lst4:
            str1=str1+i
        print(str1)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)