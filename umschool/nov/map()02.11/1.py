with open("1.txt") as file:
    s = file.readline()

    def f(x):
        return (int(x) % 7) ** 2

    print(sum(list(map(f, s.split()))))
