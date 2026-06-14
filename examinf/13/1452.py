import ipaddress

net = ipaddress.ip_network("67.187.123.42/255.255.224.0", strict=False)
min_host = min(net.hosts())

print("".join(str(min_host).split(".")))
