import ipaddress

ip1 = int(ipaddress.IPv4Address("126.115.78.15"))
ip2 = int(ipaddress.IPv4Address("126.115.84.26"))

mx = 0
for mask_len in range(33):
    net1 = ipaddress.ip_network(f"126.115.78.15/{mask_len}", strict=False)
    net2 = ipaddress.ip_network(f"126.115.84.26/{mask_len}", strict=False)
    if net1 == net2:
        mx = mask_len

net = ipaddress.ip_network(f"126.115.78.15/{mx}", strict=False)

c = 0
for ip in net:
    if bin(int(ip)).count("1") == 22:
        c += 1

print(c)
