with open("2.txt") as file:
    s = file.readline()

cur_len = 0
mx_len = 0
for i in range(len(s) - 1):
    if s[i] >= s[i + 1] and s[i + 1] > "5":
        cur_len += 1
        mx_len = max(mx_len, cur_len)
    else:
        cur_len = 0

print(mx_len + 1)
