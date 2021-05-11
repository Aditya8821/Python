def uncommon_str(str1,str2):
    if str1>str2:
        temp1=str1
        temp2=str2
    else:
        temp1=str2
        temp2=str1
    l=[i for i in temp1.split() if i not in temp2.split() ]
    return l
str1=input("Enter string 1: ")#str1="Geeks for Geeks" 
str2=input("Enter string 2: ")#str2= "Learning from Geeks for Geeks"
print(uncommon_str(str1,str2))