f = open("other/examinf/27/187B.txt")
n = int(f.readline())

c = [[0] * 13 for _ in range(3)]
ans = 0

for _ in range(n):
    x = int(f.readline())

    r = x % 3

    v = 0
    t = x
    while t > 0 and t % 2 == 0 and v < 12:
        v += 1
        t //= 2

    tr = (3 - r) % 3
    for kv in range(12 - v, 13):
        ans += c[tr][kv]

    c[r][v] += 1

print(ans)
