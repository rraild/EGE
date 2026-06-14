def to_base(n, base):
    s = []
    while n:
        n, r = divmod(n, base)
        s.append(r)
    return s


N = (
    2 * 6144**2030
    + 1536**2029
    - 2 * 384**2028
    + 96**2027
    - 2 * 24**2026
    - 2304
)
digits = to_base(N, 24)
print(sum(d > 7 for d in digits))
