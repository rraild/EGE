with open("26.txt") as f:
    lines = f.readlines()

N, K, M = map(int, lines[0].split())
t = [tuple(map(int, x.split())) for x in lines[1:]]
t.sort()
i = 0
while i < N and t[i][1] < K:
    i += 1
if i == N:
    print(0)
else:
    p = i
    while True:
        np = p
        for j in range(p + 1, min(p + M + 1, N)):
            if t[j][1] >= K:
                np = j
        if np == p:
            break
        p = np
    print(t[p][0])
