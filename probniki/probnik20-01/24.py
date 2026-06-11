import re

with open("probniki/probnik20-01/input/24.txt") as f:
    s = f.read().strip()
    r = re.findall(r"(?:[1-9][0-9]*)(?:[-*][1-9][0-9]*)*", s)
    res = max(len(m) for m in r)
    print(res)
