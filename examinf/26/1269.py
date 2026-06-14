with open("other/examinf/26/1269.txt") as f:
    line1 = f.readline().split()
    n, k = int(line1[0]), int(line1[1])
    cands = []
    for _ in range(n):
        d = list(map(int, f.readline().split()))
        total = sum(d[1:])
        interview = d[4]
        cid = d[0]
        cands.append((total, interview, cid))

    cands.sort(key=lambda x: (-x[0], -x[1], x[2]))

    if k < n and cands[k - 1][0] == cands[k][0]:
        semi_score = cands[k - 1][0]
        semi_count = 0
        for c in cands:
            if c[0] == semi_score:
                semi_count += 1

        passing_score = -1
        for i in range(k - 1, -1, -1):
            if cands[i][0] > semi_score:
                passing_score = cands[i][0]
                break
    else:
        semi_count = 0
        passing_score = cands[k - 1][0]

    last_id = -1
    for c in cands:
        if c[0] == passing_score:
            last_id = c[2]

print(last_id, semi_count)
