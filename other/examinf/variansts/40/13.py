import ipaddress

ct = 0
for i in ipaddress.ip_network("111.194.0.0/255.254.0.0", strict=False):
    b = f"{int(i):032b}"

    if (b.count("0") - b.count("1")) % 2 == 0:
        ct += 1

print(ct)
