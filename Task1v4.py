import math


def main(y, x, z):
    return math.sqrt(46*y**6 - (8*x - z**3 - 1)**3) + \
        math.sqrt(94*x**3 + math.sin(45*z + 80*y**3 + 1)**6)


print(main(-0.78, 0.04, 0.35))
