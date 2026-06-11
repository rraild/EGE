from fnmatch import fnmatch

res = []
for x in range(0, 10**8, 98):
    if fnmatch(str(x), "12*678?"):
        res.append(x)

print(max(res), max(res) // 98)
