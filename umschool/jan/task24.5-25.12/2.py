import re

with open("jan/task24.5-25.12/2.txt") as f:
    s = f.readline()
    res = re.findall(r"[123][0123]*(?:[+*][123][0123]*)*", s)
    print(len(max(res, key=len)))
