with open("jan/task24.5-25.12/1.txt") as f:
    s = "RO" + f.readline() + "RO"
    ind_RO = [i for i in range(len(s)) if s[i : i + 2] == "RO"]
    res = []
    for i in range(len(ind_RO) - 359):
        res.append(ind_RO[i + 359] - ind_RO[i])

    print(max(res))
