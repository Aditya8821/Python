import re
s='https://www.geeksforgeeks.org/'
Protocal_Name=re.findall('(\w+)://',s)
Host_Name=re.findall('://www.([\w\-\.]+)',s)
print(Protocal_Name)
print(Host_Name)
