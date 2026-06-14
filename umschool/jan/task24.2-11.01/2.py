with open("jan/task24.2-11.01/2.txt") as f:
    max_value = -1
    for line in f:
        try:
            val = eval(line)
            if val > max_value:
                max_value = val
        except Exception:
            pass

    print(max_value)
