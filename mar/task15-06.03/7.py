mx = 0

for x in range(0, 701):
    for y in range(0, 701):
        if not (x < 5 * y) and not (x > 700):
            val = x * y
            if val > mx:
                mx = val

print(mx + 1)
