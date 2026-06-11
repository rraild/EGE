def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


def dels_(d):
    dls = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            if str(x)[-2:] == "11" and x != 11:
                dls.append(x)
        if str(d // x)[-2:] == "11":
            dls.append(d // x)

    return sorted(set(dls))


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1
