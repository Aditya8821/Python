def mirror(input,k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictchar=dict(zip(original,reverse))
    prefix=input[0:k-1]
    suffix=input[k-1:]
    mirror=''
    for i in range(len(suffix)):
        mirror+=dictchar[suffix[i]]
    print(prefix+mirror)
input="paradox"
k=3
mirror(input,k)
        
