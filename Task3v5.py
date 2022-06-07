import math


def main(a, b, m):
    storage = 0.
    for j in range(1, m + 1):
        for c in range(1, b + 1):
            for i in range(1, a + 1):
                storage += (35 * i ** 2 - 14 * j ** 3) / 56 - 63 * c ** 3 - 44 * c ** 5
    return storage


print(main(5, 6, 4))
