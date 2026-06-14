T = 167


def g(s, p, end):

    if p == 1:
        return (s + 9 >= T) or (s * 3 >= T)

    if p == 2:
        return (not g(s, 1, end)) and g(s + 9, 1, end) and g(s * 3, 1, end)

    if p == 3:
        return g(s + 9, 2, end) or g(s * 3, 2, end)


S20 = []
for S in range(1, 131):
    if g(S, 3, 3):
        S20.append(S)

print(min(S20), max(S20))
