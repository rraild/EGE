mx = 0

for x in range(1, 50001):
    y = (100000 - 2 * x) // 5
    if y > 0:
        A = max(4 * y, 2 * x) + 1
        if A > mx:
            mx = A

print(mx)
