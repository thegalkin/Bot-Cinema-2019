def sis(b):
    lpos = b.find("(")
    rpos = b.find(")")
    if lpos != -1:
        stem = b[lpos + 1:rpos]
        b = b[:lpos]
        b = int(b, int(stem))
    return b



a = "56(8) + 10(2) + 28"
b = a.split(" ")
print(b)
for i, item in enumerate(b):
    if i != ",":
        if i != "+" or i!= "-" or i!= "/" or i!= "*" or i!= "^" :
            b[i] = sis(item)
        else:
            pass

    else:
        endPos = b.find(",")
        break
def priori(b):
    while True:
        if "*" in b:
            return b.index("*"), "u"
        if "/" in b:
            return b.index("/"), "d"
        if "+" in b:
            return b.index("+"), "s"
        if "-" in b:
            return b.index("-"), "m"
        if "^" in b:
            return b.index("^"), "st"

def calc(b):
    while " " in b:
        objPos, move = priori(b)
        if move == "u":
            b[objPos] = b[objPos-1] * b[objPos+1]
            del(b[objPos-1])
            del(b[objPos+1])
        if move == "d":
            b[objPos] = b[objPos-1] / b[objPos+1]
            del(b[objPos-1])
            del(b[objPos+1])
        if move == "s":
            b[objPos] = b[objPos-1] + b[objPos+1]
            del(b[objPos-1])
            del(b[objPos+1])
        if move == "m":
            b[objPos] = b[objPos-1] - b[objPos+1]
            del(b[objPos-1])
            del(b[objPos+1])
        if move == "st":
            b[objPos] = b[objPos-1] ** b[objPos+1]
            del(b[objPos-1])
            del(b[objPos+1])






print(b)
