def count_frequency(list):
    b={}
    for sublist in list:
        if len(sublist) not in b:
            b[len(sublist)]=1
        else:
            b[len(sublist)]+=1
    return b    
list=[[6, 3, 1],[8, 9],[2],[10, 12, 7],[4, 11]]
print(count_frequency(list))
