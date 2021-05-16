import re
def check(string,substring):
    if substring in string:
        y='^'+substring
        if re.search(y,string):
            print("YES")
        else:
            print("NO")
    else:
        print("Entered Substring Not in String")
string="geeks for geeks makes learning easy"
substring="geeks"
check(string,substring)
substring="makes"
check(string,substring)
