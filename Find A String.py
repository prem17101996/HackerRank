def count_substring(string, sub_string):
    c=0
    x=len(sub_string)
    for i in range(len(string)):
        if sub_string== string[i:i+x]:
            c+=1

    return(c)


