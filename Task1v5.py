import math


def main(x, y):
    return 61*(42*y**3 + x + 91*y**2)**7 - \
         (math.log2(2*y**3 + x) + 68*math.acos(65*x**2)**6)


print(main(-0.06, 0.57))
