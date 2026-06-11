for n in range(14620, 15000 + 1):
    dels = []
    for i in range(2, n):
        if n % i == 0:
            dels.append(i)
    if len(dels) == 3:
        print(n, min(dels))
