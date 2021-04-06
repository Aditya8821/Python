def remove_ith_char(i,str):
    a=str[:i]
    b=str[i+1:]
    return a+b
str= "geeksFORgeeks"
i=5
print(remove_ith_char(i,str))
