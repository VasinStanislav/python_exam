import math


def main(z):
    return math.sqrt((math.fabs(1 + z**3 + 11*z)**3 +
                     math.ceil(9 - 85*z**3 - 42*z**2)**4) / (10*z)) + \
                     z**3 / 6 + 62 * (z**2 / 6 + z)**4


print(main(0.57))
