f = open("umschool/jun/task26-16.06/5.txt")
n = int(f.readline())
phones = []
for i in range(n):
    slp, act = map(int, f.readline().split())
    phones += [(i + 1, slp, "O")]
    phones += [(i + 1, act, "A")]

phones.sort(key=lambda x: x[1])
r = [0] * n
st = 0
en = -1
for x in phones:
    id, time, params = x
    if id in r:
        continue
    if params == "O":
        r[st] = id
        st += 1
        res2 = n - st

    else:
        r[en] = id
        res2 = abs(en) - 1
        en -= 1

    res1 = id
print(res1, res2)
