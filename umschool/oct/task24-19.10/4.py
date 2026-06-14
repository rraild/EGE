with open("task24-19.10/4.txt") as file:
    s = file.readline()
    ind_XZ = []
    for i in range(len(s)):
        if s[i : i + 2] == "XZ":
            ind_XZ.append(i)

    res = []
    for i in range(len(ind_XZ) - 28):
        res.append(ind_XZ[i + 28] - ind_XZ[i] + 2)

    print(min(res))
