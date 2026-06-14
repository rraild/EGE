f = open("task24-26.10/2.txt")
max_len = 0

for s in f:
    if s.count("a") < 20:
        for i in range(len(s)):
            max_len = max(max_len, s.rindex(s[i]) - s.index(s[i]))

print(max_len)
