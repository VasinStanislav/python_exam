def main(z):
    if 204 <= z < 280:
        func_value = 4 * (z ** 3 / 24) ** 7
    elif 152 <= z < 204:
        func_value = z / 22 + 25 * (1 + z ** 3 / 23) ** 6 + \
                     3 * (65 * z ** 3 - 1 - z ** 2) ** 4
    elif z < 152:
        func_value = 28 * (z + z ** 3) ** 3 + 59 * \
                     (15 * z ** 2) ** 6 + z ** 5 / 70
    else:
        func_value = z ** 3 - (82 + 64 * z ** 3 + z ** 2) / 65 - 1
    return func_value
