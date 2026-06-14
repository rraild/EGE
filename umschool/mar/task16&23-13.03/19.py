import math
import sys

sys.set_int_max_str_digits(0)


def get_fib(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


f_target = get_fib(111111)
g_target = math.factorial(111111)
f_divisor = get_fib(111)

res = (f_target - g_target) // f_divisor
print(len(str(abs(res))))
