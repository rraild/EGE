results = []

for m in range(1, 13):
    s = bin(m)[2:]

    if m % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + "00"

    k = int(s, 2)
    results.append(k)

print(max(results))
