with open("jan/task24.2-11.01/1.txt") as f:
    res = []
    num = 0
    for s in f:
        num += 1
        try:
            val = eval(s.strip())
            res.append((val, num))
        except Exception:
            pass

print(max(res)[1])
