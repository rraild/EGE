import re

s = open("examinf/24/510.txt").read()
res = 0
num = r"(?:0|[1-9][0-9]*)"
zero_prod = rf"(?:{num}\*)*0(?:\*{num})*"
m = re.findall(rf"(?:{zero_prod}\+)+{zero_prod}", s)
print(len(max(m, key=len)))
