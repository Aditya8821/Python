def remove_empty_Tuple(a):
    b=[k for k in a if k!=()]
    return b
a=[(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
print(remove_empty_Tuple(a))
