def tri(n):

    result = ""

    while n > 0:

        result += str(n % 3)

        n //= 3

    return result[::-1]


def r(n):

    n3 = tri(n)

    if n % 3 == 0:

        n3 += n3[-3:]

    else:

        n3 += tri(n % 3 * 3)

    return int(n3, 3)


for n in range(1, 1000):

    if r(n) > 344:

        print(n)

        break
