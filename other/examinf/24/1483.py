import re

s = open("other/examinf/24/1483.txt").readline().replace("CDE", "#")
m = re.findall(r"(?=((?:#\w*){86}#[^E]))", s)
print(len(min(m, key=len)) + 2 * 87)
