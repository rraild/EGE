import re

with open("jan/task24.5-25.12/4.txt") as f:
    s = f.readline()
    res = re.findall(r"[345][0345]*(?:[*][345][0345]*)*", s)
    print(eval(max(res, key=eval)))
