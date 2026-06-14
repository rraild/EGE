import ipaddress

net = ipaddress.ip_network("135.13.142.29/255.255.255.128", strict=False)
max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
