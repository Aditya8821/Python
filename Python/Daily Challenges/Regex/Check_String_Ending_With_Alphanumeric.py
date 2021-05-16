import re
regex='[a-zA-Z0-9]$'
def check(string):
    if re.search(regex,string):
        print("ACCEPT")
    else:
        print("DISCARD")
check("ankirai@")
check("aditya")
check("aditya88")
check("adity.")
