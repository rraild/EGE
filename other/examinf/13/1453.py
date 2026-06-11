import ipaddress

net = ipaddress.ip_network("167.89.100.150/255.255.248.0", strict=False)

min_host = min(net.hosts())

octets = str(min_host).split(".")
print("".join(octets))
