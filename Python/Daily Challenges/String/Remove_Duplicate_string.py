def remove_duplicate_with_order(str):
    t=""
    for i in str:
        if i not in t:
            t=t+i
    print("With Order:",t)
def remove_duplicate_without_order(str):
    t=set(str)
    t="".join(t)
    print("Without Order:",t)
str="geeksforgeeks"
remove_duplicate_with_order(str)
remove_duplicate_without_order(str)