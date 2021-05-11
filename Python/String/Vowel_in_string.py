string=input("Enter string: ")
vowel="aeiou"
flag=0
for i in vowel:
    if i not in string:
        flag=1
if flag==0:
    print("Accepted")
else:
    print("Not Accepted")
