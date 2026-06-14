with open("dec/task9-22.12/2.txt") as f:
    c = 0
    for s in f:
        a, b, d = map(int, s.split())
        if (a + b + d) / 3 < 15:
            c += 1

    print(c)
