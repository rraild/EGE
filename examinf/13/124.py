import ipaddress

net = ipaddress.ip_network("135.221.128.0/255.255.128.0")
ans = min(bin(int(ip)).count("1") for ip in net)

print(ans)
