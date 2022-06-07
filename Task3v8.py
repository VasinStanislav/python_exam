import math


def main(m, a, b, z):
    storage1 = 0.
    storage2 = 0.
    for i in range(1, a + 1):
        for k in range(1, m + 1):
            storage1 += 69*(95*k**2)**3 - 91*i**5 - math.cos(i)**7
    for j in range(1, m + 1):
        for i in range(1, b + 1):
            storage3 = 1.
            for c in range(1, a + 1):
                storage3 *= (21*z + j**2)**3 - 66*i**6 - 13*c
            storage2 += storage3
    return storage1 + storage2


print(main(7, 3, 4, -0.8))
