for n in range(1, 1000):
    s = oct(n)[2:]

    if n % 2 == 0:
        max_digit = max(s)
        s = s + max_digit
    else:
        min_digit = int(min(s))
        s = s + oct(min_digit * 2)[2:]

    r = int(s, 8)

    if r < 313:
        ans = n

print(ans)
