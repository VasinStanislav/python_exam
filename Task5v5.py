import math


def main(x, y):
    storage = 0.
    n = len(x)
    for i in range(1, n):
        storage += math.sin(y[n - math.ceil(i / 3)]**2 + 58*x[i])**7
    return 13*storage


print(main([-0.22, -0.76, -0.89], [-0.14, -0.14, 0.54]))
