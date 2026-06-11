def D(n, m):
    return n % m == 0


res = []

B = list(range(45, 91))

for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        if D(x, 52) and not ((not (x in B)) or D(x, A)):
            t = False
            break

    if t:
        res.append(A)

print(len(res))
