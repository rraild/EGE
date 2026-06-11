def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start * 2, end) + f(start * 3, end)


path_14 = f(6, 14) * f(14, 48)
path_18 = f(6, 18) * f(18, 48)
path_both = f(6, 14) * f(14, 18) * f(18, 48)

print(path_14 + path_18 - path_both)
