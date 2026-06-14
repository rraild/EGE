for x in "0123456789ABCDEFGHI":
    num1 = int(f"55{x}36", 19)
    num2 = int(f"{x}2524", 19)
    total = num1 + num2
    if total % 11 == 0:
        print(x, total // 11)
        break
