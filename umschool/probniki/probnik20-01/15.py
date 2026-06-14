Q = list(range(260, 520, 10))
P = list(range(100, 360, 10))
A = []

for x in range(1, 10000):
    x = x / 10
    if not ((((x in P) <= (not (x in Q))) or (x in A))):
        A.append(x)

print([x // 10 for x in A])
print(35 - 26)
