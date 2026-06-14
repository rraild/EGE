import re

with open("jan/task24.5-25.12/3.txt") as f:
    s = f.readline()
    res = re.findall(r"[234][0234]*(?:[+*][234][0234]*)*", s)
    print(len(max(res, key=len)))
