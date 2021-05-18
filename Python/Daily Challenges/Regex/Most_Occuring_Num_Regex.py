import re
from collections import Counter
def Most_Occuring_Ele(word):
    arr=re.findall(r'[0-9]+',word)
    All_Ele_Freq=Counter(arr)
    Max_Ele=max(All_Ele_Freq,key=All_Ele_Freq.get)
    return Max_Ele
word = 'geek55of55gee4ksabc3dr2x'
print(Most_Occuring_Ele(word))
