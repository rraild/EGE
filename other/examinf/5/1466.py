res = []


def hex_sum_digits(s):
    hexdigits = "0123456789abcdef"
    return sum(hexdigits.index(d) for d in s)


for n in range(3, 1000):
    h = hex(n)[2:]
    s_digits = hex_sum_digits(h)

    if s_digits % 2 == 0:
        h = h + "f"
    else:
        h = h + "1"

    r = int(h, 16)
    if r <= 300:
        res.append(n)

print(max(res))
