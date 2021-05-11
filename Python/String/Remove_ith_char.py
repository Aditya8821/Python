s=input("Enter string:- ")
i=int(input("Enter ith number:- "))
r="".join([s[k] for k in range(len(s)) if k!=i-1])
print(r)