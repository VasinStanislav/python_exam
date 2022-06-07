import math


def main(a, n, b):
    storage1 = 0.
    storage2 = 1.
    for c in range(1, a + 1):
        storage1 += c**7 - 34*c**3
    for i in range(1, b + 1):
        storage3 = 0.
        for k in range(1, a + 1):
            for j in range(1, n + 1):
                storage3 += 83*(0.02 + j)**3 - i**7 / 73 - 75*math.ceil(k - 1)**6
        storage2 *= storage3
    return storage1 + storage2


print(main(3, 8, 6))
