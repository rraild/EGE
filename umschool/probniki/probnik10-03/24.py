import re

with open("probniki/probnik10-03/24.txt") as f:
    text = f.read()

    m = re.findall(r"[1-9AB][0-9AB]*[13579B]|[13579B]", text)

    print(max(len(m) for m in m))
