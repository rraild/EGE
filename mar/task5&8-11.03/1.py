results = []

for n in range(2, 500):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = s + s[-2:]
    else:
        s = "1" + s + "0"

    r = int(s, 2)
    if r > 320:
        results.append(r)


print(min(results))
