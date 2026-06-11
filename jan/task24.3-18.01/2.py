import re

with open("jan/task24.3-18.01/2.txt") as f:
    s = f.readline()
    r = re.findall(r"[0-9+-/*=()]+", s)
    print(len(max(r, key=len)))
