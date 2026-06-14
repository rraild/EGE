r = 0
with open("task24-26.10/1.txt") as f:
    for l in f:
        s = l.strip()
        print(s)
        a = sum(1 for i in range(len(s) - 1) if s[i : i + 2] == "AB")
        c = s.count("C")
        if a > 1 and c > 1 and a >= c:
            r += 1
print(r)
