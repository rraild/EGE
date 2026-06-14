import re

f = open("other/examinf/24/1646.txt").readline()
matches = re.findall(r"[1-9ABCD][0-9ABCD]*[02468AC]", f)
print(len(max(matches, key=len)))
