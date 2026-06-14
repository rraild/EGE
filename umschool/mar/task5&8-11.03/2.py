results = []

for n in range(42, 500):
    s = bin(n)[2:]
    sum_digits = s.count("1")

    if sum_digits % 2 == 0:
        s = s + "1"
        s = "11" + s[2:]
    else:
        s = s + "1"
        s = "10" + s[2:]

    r = int(s, 2)
    results.append(r)

print(min(results))
