mn = float("inf")

for x in range(120000, 120001):
    for y in range(120000, 120001):
        cur_sm = y + 4 * x
        if cur_sm < mn:
            mn = cur_sm

ans = mn - 1
print(ans)
