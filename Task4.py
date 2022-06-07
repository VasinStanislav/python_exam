def main(n):
    if n >= 2:
        func_value = main(n - 2) ** 3 / 34 - main(n - 2) ** 2 - \
                     (main(n - 2) - 17 * main(n - 1) ** 2) / 41
    elif n == 1:
        func_value = -0.35
    else:
        func_value = 0.86
    return func_value
