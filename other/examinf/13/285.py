import ipaddress

net = ipaddress.ip_network("139.75.100.0/255.255.252.0", strict=False)
c = 0

for ip in net:
    last_octet = int(ip) % 256
    if last_octet in (1, 3, 7, 15, 31, 63, 127, 255):
        c += 1

print(c)
