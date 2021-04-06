def sort_list(x,y):
    zipped_pairs = zip(y,x)
    z = [i[1] for i in sorted(zipped_pairs)]
    return z
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print(sort_list(x, y))
 

