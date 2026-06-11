with open("task24-19.10/7.txt") as file:
    s = file.readline()

    parts = s.split("E")

    mx_len = 0
    for part in parts:
        left = 0
        cnt_C = 0
        for right in range(len(part)):
            if part[right] == "C":
                cnt_C += 1
            while cnt_C > 300:
                if part[left] == "C":
                    cnt_C -= 1
                left += 1
            mx_len = max(mx_len, right - left + 1)

    print(mx_len)
