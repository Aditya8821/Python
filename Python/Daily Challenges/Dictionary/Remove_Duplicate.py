from collections import Counter
def remDup(input):
    input=input.split(" ")
    Uniq=Counter(input)
    res=" ".join(Uniq.keys())
    print(res)
input = 'Python is great and Java is also great'
remDup(input)
