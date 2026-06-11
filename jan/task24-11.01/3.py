import re

with open("jan/task24-11.01/3.txt") as f:
    s = f.readline()
    numbers = re.findall(r"[0-9A-G]+", s)
    print(max(len(num) for num in numbers))
