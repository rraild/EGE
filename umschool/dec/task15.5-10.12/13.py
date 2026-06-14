def U(a, b, c):
    return a + b + c == 180


res = []

for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        if not (U(47, A, x + 40) == (U(A, x, 45) and (not (A + 30 < 156)))):
            t = False
            break
    if t:
        res.append(A)

print(min(res))
