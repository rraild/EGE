import re

with open("jan/task24.5-25.12/5.txt") as f:
    s = f.readline()
    res = re.findall(r"[789][0789]*(?:[*][789][0789]*)*", s)
    print(eval(max(res, key=eval)))
