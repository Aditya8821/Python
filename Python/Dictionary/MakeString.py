from collections import Counter
def makestring(str1,str2):
    dict1=Counter(str1)
    dict2=Counter(str2)
    res=dict1 & dict2
    return res==dict1
str1 = 'ABHISHEKsinGH'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
if(makestring(str1,str2)==True):
    print("POSSIBLE")
else:
    print("NOT POSSIBLE")
