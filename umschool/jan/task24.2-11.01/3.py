import re

max_val = -1

with open("jan/task24.2-11.01/3.txt") as f:
    for s in f:
        s = s.strip()

        line = re.sub(r"-\d+", "", s)
        line = line.lstrip("+*").rstrip("+*")

        try:
            val = eval(line)
            if val > max_val:
                max_val = val
        except Exception:
            pass

print(int(max_val))
