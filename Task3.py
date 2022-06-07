import math


def main(m, a, p):
    func_value = 0
    for i in range(1, a + 1):
        for j in range(1, m + 1):
            func_value += j ** 2 - math.log10(p) - 73 * i ** 4
        func_value -= 39 * i ** 7 + math.exp(i)
    return func_value
