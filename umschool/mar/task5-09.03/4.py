rs = []

for n in range(1, 1000):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = s + s[:2]
    else:
        s = "1" + s + "1"

    r = int(s, 2)
    if r > 700:
        rs.append(r)

print(min(rs))
