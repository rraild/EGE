min_R = float("inf")

for N in range(1, 1000):
    digits = []
    n = N
    while n > 0:
        digits.append(n % 13)
        n //= 13
    if not digits:
        digits = [0]
    s = "".join(
        str(d) if d < 10 else chr(ord("A") + d - 10) for d in digits[::-1]
    )

    last_c = s[-1]
    last_d = int(last_c) if last_c.isdigit() else 10 + ord(last_c) - ord("A")

    if last_d % 2 == 0:
        s = s + "B"
        s = "1A" + s[2:]
    else:
        s = s + "A"
        s = "21" + s[2:]

    R = int(s, 13)

    if R > 862 and R < min_R:
        min_R = R

print(min_R)
