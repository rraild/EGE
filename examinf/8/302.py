import itertools

vow = "ИОЕ"
con = "ТМФЙ"
c = 0

for word in itertools.product("ТИМОФЕЙ", repeat=6):
    v_c = 0
    c_c = 0
    for char in word:
        if char in vow:
            v_c += 1
        else:
            c_c += 1

    if v_c == c_c:
        c += 1

print(c)
