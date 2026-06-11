import itertools

c = 0
for i in itertools.product("0123456789ABCDE", repeat=5):
    s = "".join(x for x in i)
    if s[0] != "0" and s.count("8") == 1:
        s = s.replace("A", "*")
        s = s.replace("B", "*")
        s = s.replace("C", "*")
        s = s.replace("D", "*")
        s = s.replace("E", "*")
        if s.count("*") > 1:
            c += 1
            print(s)


print(c)
