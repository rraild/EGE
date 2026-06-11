import ipaddress

net = ipaddress.ip_network("186.135.80.0/255.255.252.0", strict=False)
count = 0

for ip in net:
    bn = f"{int(ip):032b}"

    ls = bn[:16]
    rs = bn[16:]

    if ls.count("1") > rs.count("1"):
        count += 1

print(count)
