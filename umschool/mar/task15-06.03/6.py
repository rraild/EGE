res = []

for x in range(801, 1000):
    for y in range(801, 1000):
        if not (x <= 800) and not (x > y):
            res.append(x * y)

print(min(res) - 1)
