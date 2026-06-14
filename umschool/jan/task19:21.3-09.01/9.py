def Win1(S):
    return (S + 9 >= 167) or (S * 3 >= 167)


def Loss1(S):
    return (not (Win1(S))) and Win1(S + 9) and Win1(S * 3)


def Win2(S):
    return Loss1(S + 9) or Loss1(S * 3)


def Loss12(S):
    return (
        (Win1(S + 9) or Win2(S + 9))
        and (Win1(S * 3) or Win2(S * 3))
        and (Win2(S + 9) or Win2(S * 3))
    )


S21 = []

for S in range(1, 131):
    if Loss12(S):
        S21.append(S)

print(min(S21))
