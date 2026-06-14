def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 2, end) + f(start * 4, end)


print(f(3, 200) * f(200, 510))
