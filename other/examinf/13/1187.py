import ipaddress

net = ipaddress.ip_network("158.214.121.40/255.255.255.224", strict=False)
min_host = min(net.hosts())

print("".join(str(min_host).split(".")))
