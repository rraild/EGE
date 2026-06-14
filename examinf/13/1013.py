import ipaddress

node_ip = "218.194.82.148"
mask = "255.255.255.192"

net = ipaddress.ip_network(f"{node_ip}/{mask}", strict=False)

mx = max(net.hosts())

print("".join(str(mx).split(".")))
