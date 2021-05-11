def split(str):
    splitted=str.split(" ")
    return splitted
def join(str):
    joined="-".join(str)
    return joined
str="Geeks For Geeks"
splitted=split(str)
print(splitted)
print(join(splitted))