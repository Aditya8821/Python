import re
"""
'^[a-z]$'=This Regular expression satisfies the condition for single char string
'^([a-z]).*\1$'=This Regular expression satisfies the condition for multiple char string
"""
regex = r'^[a-z]$|^([a-z]).*\1$'
def check(string):
    if(re.search(regex, string)):  
        print("Valid")  
    else:  
        print("Invalid")  
sample1 = "abba"
sample2 = "a"
sample3 = "abcd"
check(sample1)
check(sample2)
check(sample3)
