from fnmatch import fnmatch

res = []
for n in range(550034, 10**8, 98):
    s = str(n)
    if fnmatch(s, "55??34*"):
        if s.count("4") == 2 and "8" not in s:
            res.append(n)

ans = max(res)
print(ans, ans // 98, sep="")
