import re
regex='^[aeiouAEIOU][A-Za-z0-9_]*'
def check(string):
    if re.search(regex,string):
        print("VALID")
    else:
        print("InValid")
check("ankit")
check("geeks")
check("Sandeep")
