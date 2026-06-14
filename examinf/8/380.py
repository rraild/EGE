import itertools

c = 0
ls = 0

for word in itertools.product(sorted("ГОНДУБШ"), repeat=6):
    c += 1
    s = "".join(word)

    if c % 2 != 0:
        if s[0] != "Б" and s.count("Н") >= 2 and "У" not in s:
            ls = c

print(ls)
