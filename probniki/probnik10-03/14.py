def f(n, b) -> str:
    s = ""
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


for x in range(0, 22):
    v1 = int(f"5AG{x}2", 22)
    v2 = int(f"6{x}2{x}7", 22)
    if f(v1 + v2, 9).count("7") == 2:
        print(x, v1 + v2)
