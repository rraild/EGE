for i in range(7777, 10**9, 7777):
    s = str(i)
    if len(s) == 9:
        if s[7:] == "77":
            if (
                int(s[0]) % 2 == 0
                and int(s[1]) % 2 != 0
                and int(s[2]) % 2 == 0
                and int(s[3]) % 2 == 0
                and int(s[4]) % 2 != 0
                and int(s[5]) % 2 == 0
                and int(s[6]) % 2 != 0
            ):
                print(i, i // 7777)
