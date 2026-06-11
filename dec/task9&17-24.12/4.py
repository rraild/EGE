with open("dec/task9&17-24.12/4.txt") as f:
    ct = 0
    for s in f:
        n = list(map(int, s.split()))
        a, b, c, d = n

        if a * b == c * d or a * c == b * d or a * d == b * c:

            mn = min(n)
            mx = max(n)

            if mx**2 <= mn * mx:
                ct += 1

    print(ct)
