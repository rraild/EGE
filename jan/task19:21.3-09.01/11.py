def win1(s):
    return (s - 3 <= 15) or (s - 5 <= 15)


ans = []
for s in range(16, 47):
    if win1(s):
        continue

    ok = False
    for m in (s - 3, s - 5):
        if m <= 15:
            continue
        if win1(m):
            continue
        if win1(m - 3) and win1(m - 5):
            ok = True
            break

    if ok:
        ans.append(s)

print(f"{min(ans)}{max(ans)}")
