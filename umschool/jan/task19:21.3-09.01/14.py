def Win1(S):
    return (S + 4 >= 101) or (S * 5 >= 101)


def Loss1(S):
    return (not Win1(S)) and Win1(S + 4) and Win1(S * 5)


def Win2(S):
    return Loss1(S + 4) or Loss1(S * 5)


S20 = []
for S in range(1, 101):
    if Win2(S):
        S20.append(S)

print(f"{min(S20)}{max(S20)}")
