for x in "0123456789ABCDEFGHIJ":
    num1 = int(f"13{x}CF", 20)
    num2 = int(f"47GH{x}", 20)
    total = num1 + num2
    if total % 19 == 0:
        print(x, total // 19)
        break
