from collections import Counter
def maxanagram(input):
    input=input.split(" ")
    for i in range(len(input)):
        input[i]="".join(sorted(input[i]))
    freqDict=Counter(input)
    print(max(freqDict.values()))
input = 'ant magenta magnate tan gnamate'
maxanagram(input)
