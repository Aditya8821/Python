def remove_empty(a):
    b=[k for k in a if k!=[]]
    return b
a=[5,6,[],3,[],5,7,[],[]]
print(remove_empty(a))
