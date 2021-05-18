import re
def match(text):
    pattern='[A-Z]+[a-z]+$'
    if re.search(pattern,text):
        print("Yes")
    else:
        print("No")
match("Geeks")
match("geeksforGeeks")
match("geeks")
