with open("dec/task9&17-24.12/1.txt") as f:
    c = 0
    for s in f:
        n = list(map(int, s.split()))
        n.sort()
        if n[0] + n[3] == n[1] + n[2]:
            print(n)
            c += 1

    print(c)
