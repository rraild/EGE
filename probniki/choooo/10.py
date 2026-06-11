ct = 0
f = open("probniki/choooo/10.txt").read().split()
for x in f:
    x.split("-")

    if x.lower()[0] == "а" and x.lower()[-1] == "я" and "-" not in x:
        ct += 1

print(ct)
