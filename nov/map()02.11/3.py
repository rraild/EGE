cnt = 0

with open("3.txt", "r") as f:
    for l in f:
        a, b, c = map(int, l.split())
        if b - a == c - b:
            cnt += 1

print(cnt)
