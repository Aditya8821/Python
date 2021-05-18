import re
def PutSpace(input):
    words=re.findall('[A-Z][a-z]*',input)
    result=[]
    for word in words:
        word=chr(ord(word[0])+32)+word[1:]
        result.append(word)
    print(" ".join(result))
input ='BruceWayneIsBatman'
PutSpace(input)
