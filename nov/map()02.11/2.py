from math import sqrt

with open("2.txt") as file:
    s = file.readline()

    def f(x):
        return int((sqrt(int(x)))) * 4

    print(sum(list(map(f, s.split()))))
