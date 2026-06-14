import re

with open("jan/task24.3-18.01/3.txt") as f:
    s = f.readline()
    r = re.findall(r"[1-9A-G]+", s)
    print(len(max(r, key=len)))
