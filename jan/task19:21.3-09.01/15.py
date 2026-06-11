def Win1(S):
    return (S + 4 >= 101) or (S * 5 >= 101)


def Loss1(S):
    return (not Win1(S)) and Win1(S + 4) and Win1(S * 5)


def Win2(S):
    return Loss1(S + 4) or Loss1(S * 5)


def Loss12(S):
    return (
        (Win1(S + 4) or Win2(S + 4))
        and (Win1(S * 5) or Win2(S * 5))
        and (Win2(S + 4) or Win2(S * 5))
    )


S21 = []
for S in range(1, 101):
    if Loss12(S):
        S21.append(S)

print(min(S21))
