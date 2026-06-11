res = []
for x in range(1, 150000):
    if (x % 512 == 0) and (x % 243 == 0):
        res.append(x)

print(res)
