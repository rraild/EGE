import ipaddress

net = ipaddress.ip_network("123.222.111.192/255.255.255.248", strict=False)
c = 0

for ip in net:
    fth = int(str(ip).split(".")[3])
    bn = f"{fth:08b}"
    if bn.count("0") % 3 != 0:
        c += 1

print(c)
