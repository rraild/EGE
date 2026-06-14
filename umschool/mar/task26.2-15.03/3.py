with open("mar/task26.2-15.03/3.txt") as f:
    n, m = map(int, f.readline().split())
    for i in range(m):
        box, ribbon = map(int, f.readline().split())
