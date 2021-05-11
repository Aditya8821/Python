txt="GeeksforGeeks"
d=2
def rotation(txt,d):
    lfirst=txt[0:d]
    lsecond=txt[d:]
    rfirst=txt[0:len(txt)-d]
    rsecond=txt[len(txt)-d:]
    print("Left Rotation:",(lsecond+lfirst))
    print("Right Rotation:",(rsecond+rfirst))
rotation(txt,d)