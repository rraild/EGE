with open("task24-19.10/6.txt") as file:
    s = "X" + file.readline() + "X"
    ind_x = []
    for i in range(len(s)):
        if s[i] == "X":
            ind_x.append(i)

    res = []
    for i in range(len(ind_x) - 60):
        if s[ind_x[i] + 1 : ind_x[i + 60]].count("2025") >= 80:
            res.append(ind_x[i + 60] - ind_x[i] - 1)

    print(max(res))
