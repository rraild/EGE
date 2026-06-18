def f(start, end):
    if start < end:
        return 0

    if start == end:
        return 1

    return f(start - 3, end) + f(start - 4, end) + f(start // 2, end)


print(
    f(78, 30) * f(30, 2)
    + f(78, 42) * f(42, 2)
    - f(78, 42) * f(42, 30) * f(30, 2)
)
