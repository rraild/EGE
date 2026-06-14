from ipaddress import ip_network

ip_net = ip_network("111.1.234.205/255.255.248.0", strict=False)

c = 0
for i in ip_net:
    if (
        f"{i:b}"[0:8].count("0") % 2 == 0
        and f"{i:b}"[8:16].count("0") % 2 != 0
        and f"{i:b}"[16:24].count("0") % 2 == 0
        and f"{i:b}"[24:32].count("0") % 2 != 0
    ) or (
        f"{i:b}"[0:8].count("0") % 2 != 0
        and f"{i:b}"[8:16].count("0") % 2 == 0
        and f"{i:b}"[16:24].count("0") % 2 != 0
        and f"{i:b}"[24:32].count("0") % 2 == 0
    ):
        c += 1

print(c)

# a = "1" * 8 + "2" * 8 + "3" * 8 + "4" * 8
# print(a[0:8], a[8:16], a[16:24], a[24:32])
