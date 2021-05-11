def countfreq(input):
    freq={}
    for i in input:
        freq[i]=input.count(i)
    for key,value in freq.items():
        print("%d:%d"%(key,value))
input=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
countfreq(input)
