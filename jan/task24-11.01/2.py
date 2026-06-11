import re

with open("jan/task24-11.01/2.txt") as f:
    s = f.readline()
    numbers = re.findall(r"[13579]+", s)
    print(max(int(num) for num in numbers))
