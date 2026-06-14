with open("task24-19.10/5.txt") as file:
    s = file.readline()
    res = []

    for l in range(len(s)):
        if s[l] not in "13579":
            continue

        cnt_r = 0
        for r in range(l + 1, len(s)):
            if s[r] == "r":
                cnt_r += 1

            if s[r] in "13579":
                break

            if cnt_r > 58:
                break

            if cnt_r == 58:
                res.append(r - l + 1)
    print(max(res))
