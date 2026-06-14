mx = 0

for n in range(2, 500):
    s = bin(n)[2:]
    sum_digits = s.count("1")

    if sum_digits % 2 == 0:
        s = s + "0"
        s = "10" + s[2:]
    else:
        s = s + "11"
        s = "11" + s[2:]

    r = int(s, 2)
    if r < 99:
        mx = max(mx, n)

print(mx)
