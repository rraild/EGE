import fnmatch

mask = "4*4736*1"
d = 7993
limit = 10**10
res = []

start = (4000000 // d) * d
if start < d:
    start = d

for x in range(start, limit + 1, d):
    s = str(x)
    if s[0] == "4" and s[-1] == "1":
        if fnmatch.fnmatch(s, mask):
            res.append((x, x // d))

res.sort()
for val, quot in res:
    print(val, quot)
