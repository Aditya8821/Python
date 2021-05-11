from itertools import permutations
def permutation(str):
    permulist=permutations(str)
    for i in permulist:
        print(" ".join(i))
str="ABCD"
permutation(str)