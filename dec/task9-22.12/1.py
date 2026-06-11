with open("dec/task9-22.12/1.txt") as f:
    c = 0
    for s in f:
        a, b, d = map(int, s.split())
        print(a, b, d)
        if a + b == d or a + d == b or b + d == a:
            c += 1

    print(c)
