txt="Geeksforgeeks is the best site to for coders"
word=["the","best","site"]
replace_word="gfg"
print("Original String ="+str(txt))
output=' '.join([replace_word if i in word else i for i in txt.split()])
print("String after replacing ="+str(output))
