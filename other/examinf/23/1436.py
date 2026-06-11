def f(start, end, count_b):
    if start > end or count_b > 3:
        return 0
    if start == end:
        return 1

    return (
        f(start + 3, end, count_b)
        + f(start + 4, end, count_b + 1)
        + f(start**2, end, count_b)
    )


print(f(4, 61, 0))
