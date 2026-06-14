from fnmatch import fnmatch

res = []
for x in range(0, 10**5, 134):
    if fnmatch(str(x), "1?7*"):
        res.append(x)

for i in res:
    print(bin(i)[2:].count("1"))
