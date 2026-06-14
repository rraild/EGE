def Win1(S):
    return (S - 3 <= 15) or (S - 5 <= 15)


S_list = []

for S in range(16, 47):
    if (S - 3 > 15 and Win1(S - 3)) or (S - 5 > 15 and Win1(S - 5)):
        S_list.append(S)

print(max(S_list))
