import re

with open("jan/task24.4-18.01/2.txt") as f:
    s = f.readline()
    r = re.findall(r"(?:-?\d+(?:[+\-*]\d+)*)", s)
    max_len = len(max(r, key=len))
    print(max_len)
