def win1(s):
    return (s + 2 >= 81) or (4 * s - 3 >= 81)


ans = []
for s in range(1, 81):
    if (s + 2 < 81 and win1(s + 2)) or (4 * s - 3 < 81 and win1(4 * s - 3)):
        ans.append(s)

print(min(ans))
