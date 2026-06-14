import re

with open("jan/task24-11.01/1.txt") as f:
    s = f.readline()
    numbers = re.findall(r"[1-9][0-9]{5,}", s)
    print(min(int(num) for num in numbers))
