from collections import Counter
def anagram(a,b):
    bin1=bin(a)[2:]
    bin2=bin(b)[2:]
    zeroes=(len(bin1)-len(bin2))
    if(len(bin1)>len(bin2)):
        bin2=zeroes*'0'+bin2
    else:
        bin1=zeroes*'0'+bin1
    dict1=Counter(bin1)
    dict2=Counter(bin2)
    if dict1==dict2:
        return "YES"
    else:
        return "NO"
a=8
b=4
print(anagram(a,b))
