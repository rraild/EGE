import re

s = open("other/examinf/24/826.txt").readline()

m = re.findall(r"A+(?:[1-9]+[-*])+\d+", s)
print(len(max(m, key=len)))
