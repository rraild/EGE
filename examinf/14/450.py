def f(n, b):
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


v = 53**123 + 65**2222 - 172**12
res = f(v, 7)

ans = 0
for d in "12345":
    ans += res.count("6" + d)

print(ans)
