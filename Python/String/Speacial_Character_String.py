import string
def special_char(str):
    special=string.punctuation
    if any(char in special for char in str):
        return "NOT ACCEPTED"
    else:
        return "ACCEPTED"
str = "Geeks$For$Geeks"
print(special_char(str))
