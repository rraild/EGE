import ipaddress

net = ipaddress.ip_network("143.168.72.213/255.255.255.240", strict=False)
max_host = max(net.hosts())

print("".join(str(max_host).split(".")))
