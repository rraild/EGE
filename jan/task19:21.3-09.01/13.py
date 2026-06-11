def win1(s):
    return (s + 4 >= 101) or (s * 5 >= 101)


ans = []
for s in range(1, 101):
    if (s + 4 < 101 and win1(s + 4)) or (s * 5 < 101 and win1(s * 5)):
        ans.append(s)

print(min(ans))
