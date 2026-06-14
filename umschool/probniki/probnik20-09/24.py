import re

with open("24_55.txt") as f:
    lines = [lins.strip() for lins in f if lins.strip()]

minw = None
t = None

for lins in lines:
    c = len(re.findall(r"W", lins))
    if minw is None or c < minw:
        minw = c
        t = lins

if t is None:
    pass
else:
    freq = {ch: t.count(ch) for ch in set(t)}
    m = max(freq.values())
    print(max(ch for ch in freq if freq[ch] == m))
