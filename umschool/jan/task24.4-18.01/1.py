import re

with open("jan/task24.4-18.01/1.txt") as f:
    s = f.readline()
    r = re.findall(r"(?:XYZ)+(?:LD?)?", s)
    print(len(max(r, key=len)))
