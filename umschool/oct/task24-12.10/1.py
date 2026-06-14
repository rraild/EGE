with open("task24-12.10/1.txt") as file:
    s = file.readline()
    ind_K = []
    for i in range(len(s) - 1):
        if s[i] == "K":
            ind_K.append(i)

    res = []
    for i in range(len(ind_K) - 309):
        res.append(ind_K[i + 309] - ind_K[i] + 1)

    print(min(res))
