import re

file = open(r"other/examinf/24/987.txt").readline()


match = re.findall(r"A[^AD]*D", file)
match2 = re.findall(r"D[^AD]*A", file)
print(len(max(match, key=len)))
print(len(max(match2, key=len)))
