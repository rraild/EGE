import re

f = open("jan/task24.4-18.01/3.txt")

valid = []

for s in f:
    s = s.strip()
    if re.fullmatch(r"^\d+([+\-*]\d+)*$", s):
        valid.append(s)

print(len(valid))
