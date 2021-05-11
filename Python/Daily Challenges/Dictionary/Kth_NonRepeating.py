from collections import OrderedDict
def rep(input,k):
   dict=OrderedDict.fromkeys(input,0)
   for ch in input:
       dict[ch]+=1
   nonrep=[key for (key,value) in dict.items() if value==1]
   if len(nonrep)<k:
       return "Less than k non-repeating char in input"
   else:
       return nonrep[k-1]
input = "geeksforgeeks"
k=3
print(rep(input,k))
