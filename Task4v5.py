def main(n):
    if n == 0:
        return -0.09
    if n == 1:
        return -0.15
    if n >= 2:
        return main(n - 2)**2 + main(n - 1)**2


print(main(8))
