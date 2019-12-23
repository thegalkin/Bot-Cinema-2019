a = "56(8) + 10(2) + 28"
b = a.split(" ")
print(b)
for i in b:
    if i != ",":
        if i != "+" or i!= "-" or i!= "/" or i!= "*" or i!= "^" :
            i = sis(i)
        else:
            pass

    else:
        endPos = b.find(",")
        break
def sis(b):
    for i in range(b):
        lpos = -1
        unchanged = b
        if b[i] == "(":
            lpos = i
        if b[i] == ")":
            rpos = i
        if lpos != -1:
            stem = b[lpos+1:rpos]
            b = b[:lpos]
            b = int(b, stem)
    return b





print(int(a, 8))
