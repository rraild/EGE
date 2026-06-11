def Win1(S):
    return (S + 2 >= 81) or (S * 4 - 3 >= 81)


def Loss1(S):
    return (not Win1(S)) and Win1(S + 2) and Win1(S * 4 - 3)


def Win2(S):
    return Loss1(S + 2) or Loss1(S * 4 - 3)


def Loss12(S):
    return (
        (Win1(S + 2) or Win2(S + 2))
        and (Win1(S * 4 - 3) or Win2(S * 4 - 3))
        and (Win2(S + 2) or Win2(S * 4 - 3))
    )


S21 = []
for S in range(1, 81):
    if Loss12(S):
        S21.append(S)

print(min(S21))
