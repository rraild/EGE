def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1

    first_digit_sq = int(str(start**2)[0])
    sum_digits = sum(int(d) for d in str(start))

    return f(start - first_digit_sq, end) + f(start - sum_digits, end)


print(f(32, 1))
