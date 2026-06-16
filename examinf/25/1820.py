def check_pow(n):
    val = 7**n
    return val if val < 8700000 else False


count = 0

for i in range(8699999, 0, -1):
    if "1" in str(i) or "3" in str(i):
        for k in range(1, 10):
            pow7 = check_pow(k)
            if not pow7:
                break

            a = i - pow7
            if a > 0:
                root = a**0.5
                if root.is_integer() and int(root) % 2 == 0:
                    print(i, k)
                    count += 1
                    break

        if count == 5:
            break
