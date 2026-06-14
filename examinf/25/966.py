for mid_len in range(6):
    for mid in range(10**mid_len):
        star = str(mid).zfill(mid_len)

        for d in "0123456789":
            s = f"32{star}54{d}123"

            if len(s) % 2 != 0:
                continue

            if "0" in s:
                continue

            n = len(s) // 2

            if sum(map(int, s[:n])) != sum(map(int, s[n:])):
                continue

            num = int(s)

            if num % 519 == 0:
                print(num, num // 519)
