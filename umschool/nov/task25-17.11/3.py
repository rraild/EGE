from fnmatch import fnmatch

res = []
for x in range(0, 10**8, 31):
    if fnmatch(str(x), "123*578"):
        res.append(x)

print(max(res), max(res) // 31)
