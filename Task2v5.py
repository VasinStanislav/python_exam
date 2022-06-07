import math


def main(y):
    if y < 131:
        return 1 + math.tan(y)**2 + 29*y**12
    elif y < 208:
        return 43*(42*y**2 - 1)**2
    else:
        return math.tan(y)**6 - 61*y**3 - 1


print(main(160))
