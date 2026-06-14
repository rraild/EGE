def g(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return g(start + 2, end) + g(start * 5, end)


print(g(2, 50))
