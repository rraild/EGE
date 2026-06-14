for x in "0123456789ABCD":
    for y in "0123456789ABCD":
        num1 = int(f"ABCD3{y}2{x}1", 14)
        num2 = int(f"192{x}9", 14)
        total = num1 + num2
        if total % 107 == 0:
            print(x, total // 107)
            break
