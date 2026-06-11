with open("other/examinf/24/1397.txt") as f:
    s = f.read().strip()

idx = []
p = s.find("RSQ")
while p != -1:
    idx.append(p)
    p = s.find("RSQ", p + 1)

n = 130
res = float("inf")

for i in range(len(idx) - n + 1):
    st = idx[i]
    en_q = idx[i + n - 1] + 2

    if en_q + 1 < len(s):
        j = en_q + 1
        while j < len(s) and s[j] == "Q":
            j += 1
        if j < len(s):
            cur = j - st + 1
            if cur < res:
                res = cur

print(res)
