s = open("3.txt").readline()
cur_len = 0
mx_len = 0
for i in range(len(s) - 1):
    if (
        s[i].isdigit()
        and s[i + 1].isdigit()
        and int(s[i]) % 2 != int(s[i + 1]) % 2
    ):
        cur_len += 1
        mx_len = max(mx_len, cur_len)
    else:
        cur_len = 0


print(mx_len + 1)
