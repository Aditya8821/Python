def binary_or_not(str):
    binary="01"
    return all([num in binary for num in str])
str="001021010001010"
if binary_or_not(str):
    print("Binary")
else:
    print("Not Binary")