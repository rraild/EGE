import ipaddress

net = ipaddress.ip_network("172.45.12.200/255.255.240.0", strict=False)
max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
