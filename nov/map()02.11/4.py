cnt = 0

with open("4.txt", "r") as f:
    for l in f:
        a, b, c = map(int, l.split())
        s = (a % 3) + (b % 3) + (c % 3)
        if s == 5:
            cnt += 1

print(cnt)
