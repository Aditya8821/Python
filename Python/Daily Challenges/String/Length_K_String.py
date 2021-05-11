def string_k(k,sentence):
    str=sentence.split(" ")
    res=[]
    res=[word for word in str if len(word)>k]
    return res
k = 3
sentence ="geek for geeks"
print(string_k(k,sentence))
