res = 0

for x in range(1, 1001):
    f = (x % 2 == 0) <= (x % 13 != 0)

    if not f:
        res = max(res, 1000 - x)

print(res)
