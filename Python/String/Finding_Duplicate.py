def duplicate(string):
    dup_list=[]
    for str in string:
        if string.count(str) >1 and str not in dup_list:
            print(str)
            dup_list.append(str)
        
string="geeksforgeeks"
duplicate(string)