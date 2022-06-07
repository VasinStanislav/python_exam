import math


def main(z, x):
    func_value = math.sin(z ** 2 - x - 0.01) / \
                 (45 * (42 * x ** 2) ** 3 - 76 * z ** 4) - math.sqrt(
        math.fabs(92 * z ** 3 - 95 * z ** 2) -
        math.log2(1 + z + x ** 2) ** 3
    )
    return func_value
