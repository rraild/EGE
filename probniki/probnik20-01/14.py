for x in range(9):
    num1 = int(f"2{x}{x}86", 9)
    num2 = int(f"72{x}38", 9)
    total = num1 + num2
    if total % 14 == 0:
        print(total // 14)
        break
