for x in "0123456789ABCDEFGH":
    num1 = int(f"AB5{x}3", 18)
    num2 = int(f"EF{x}13", 18)
    total = num1 + num2
    if total % 17 == 0:
        print(x, total // 17)
        break
