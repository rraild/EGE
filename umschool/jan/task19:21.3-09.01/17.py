def Win1(S):
    return (S + 2 >= 81) or (S * 4 - 3 >= 81)


def Loss1(S):
    return (not Win1(S)) and Win1(S + 2) and Win1(S * 4 - 3)


def Win2(S):
    return Loss1(S + 2) or Loss1(S * 4 - 3)


S20 = []
for S in range(1, 81):
    if Win2(S):
        S20.append(S)

print(f"{min(S20)}{max(S20)}")
