with open("task24-19.10/2.txt") as file:
    s = "O" + file.readline() + "O"
    ind_O = []

    for i in range(len(s)):
        if s[i] == "O":
            ind_O.append(i)

    res = []

    for i in range(len(ind_O) - 151):
        res.append(ind_O[i + 151] - ind_O[i] + 1)

print(max(res))
