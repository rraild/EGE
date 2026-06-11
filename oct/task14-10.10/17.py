m = 0
r = 0
for b in range(5, 1000):
    n = 49 * 52**32 + 33**123 + 74 * 43**121 - 751235
    c = 0
    while n > 0:
        if n % b == 4:
            c += 1
        n //= b
    if c > m:
        m = c
        r = b
    elif c == m and b > r:
        r = b
print(r)
