import re

with open("jan/task24.3-18.01/1.txt") as f:
    s = f.readline()
    r = re.findall(r"[A-Z]+", s)
    print(len(max(r, key=len)))
