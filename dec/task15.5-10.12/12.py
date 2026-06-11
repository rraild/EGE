def T(n, m, k):
    return n + m > k and n + k > m and m + k > n


def M(a, b):
    return a if a > b else b


res = []

for A in range(1, 1000):
    t = True
    for x in range(1, 1000):
        if (T(x, 11, 24) == (not (M(x, 7) > 32))) and T(x, A, 7):
            t = False
            break
    if t:
        res.append(A)

print(max(res))
