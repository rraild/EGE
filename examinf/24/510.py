import re

s = open("other/examinf/24/510.txt").read()
res = 0

ch = re.findall(r"[0-9+*]+", s)

for c in ch:
    for i in range(len(c)):
        if c[i] in "+*":
            continue
        for j in range(i + res, len(c)):
            sub = c[i : j + 1]
            if sub[-1] in "+*":
                continue

            if "++" in sub or "**" in sub or "+*" in sub or "*+" in sub:
                break

            p = re.split(r"[+*]", sub)
            if any(len(p) > 1 and p[0] == "0" for p in p):
                break

            t = True
            for add in sub.split("+"):
                if "0" not in re.split(r"[*]", add):
                    t = False
                    break

            if t:
                res = max(res, len(sub))
            elif "+" in sub:
                pass
            elif "0" not in sub:
                break

print(res)
