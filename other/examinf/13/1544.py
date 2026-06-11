import ipaddress

net = ipaddress.ip_network("95.24.16.0/255.255.240.0", strict=False)

mx = -1
target_ip = None

for ip in net:
    if ip == net.network_address or ip == net.broadcast_address:
        continue

    c1 = bin(int(ip)).count("1")

    if c1 >= mx:
        mx = c1
        target_ip = ip

octets = [int(x) for x in str(target_ip).split(".")]
print(octets[2] + octets[3])
