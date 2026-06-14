with open("task24-19.10/3.txt") as file:
    s = "RO" + file.readline() + "RO"
    ind_RO = []

    for i in range(len(s)):
        if s[i : i + 2] == "RO":
            ind_RO.append(i)

    res = []

    for i in range(len(ind_RO) - 359):
        res.append(ind_RO[i + 359] - ind_RO[i])


print(max(res))
