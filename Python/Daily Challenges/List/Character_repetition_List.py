def character_repetition(list,rep_list):
    b=["".join(letter*num for letter in word) for num in rep_list for word in list]
    return b
list = ["gfg", "is", "best"]
rep_list=[3,5,2]
print(character_repetition(list,rep_list))
