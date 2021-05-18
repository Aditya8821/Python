import re
def ExtractMax(input):
    Numbers_List=re.findall('\d+',input)
    Numbers_List=map(int,Numbers_List)
    return max(Numbers_List)
input = '100klh564abc365bg'
print(ExtractMax(input))
