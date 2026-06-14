import re

s = open("other/examinf/24/731.txt").readline()

print(len(max(re.findall(r"[C-Z]+A[C-Z]+B[C-Z]+", s), key=len)))
