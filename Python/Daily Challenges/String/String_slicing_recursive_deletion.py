def slice(input,pattern):
    if len(input)==0 and len(pattern)==0:
        return "False"
    if len(pattern)==0:
        return "False"
    while(len(input)!=0):
        index=input.find(pattern)
        if index==-1:
            return "False"
        input=input[0:index]+input[index+len(pattern):]
    return "True"
input="GEEGEEKSKS"
pattern="GEEKS"
print(slice(input,pattern))