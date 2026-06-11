import re

s = open("other/examinf/24/1125.txt").readline()

m = re.findall(r"[a-z]+@[a-z]+.[a-z]+", s)
print(len(max(m, key=len)))
