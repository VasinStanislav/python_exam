import math


def main(z, x):
    func_value = 0
    for i in range(0, len(z)):
        func_value += math.tan(x[math.floor(i/4)] + 26 * z[i] ** 3 + 1) ** 7
    func_value *= 30
    return func_value
