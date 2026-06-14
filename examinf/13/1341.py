import ipaddress

net = ipaddress.ip_network("98.112.180.225/255.255.240.0", strict=False)
max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
