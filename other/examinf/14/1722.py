def to27(n):
    r = []
    while n > 0:
        r.append(n % 27)
        n //= 27
    return r[::-1]


s = to27(
    2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561
)
print(len(list(d for d in s if d > 9)))
