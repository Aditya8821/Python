import re
string = "ThisIsGeeksforGeeks !, 123"
uppercase_char=re.findall(r"[A-Z]",string)
lowercase_char=re.findall(r"[a-z]",string)
numeric_char=re.findall(r"[0-9]",string)
special_char=re.findall(r"[,. !@$#%^&*()]",string)
print("The no. of uppercase characters is", len(uppercase_char))
print("The no. of lowercase characters is", len(lowercase_char))
print("The no. of numerical characters is", len(numeric_char))
print("The no. of special characters is", len(special_char))
