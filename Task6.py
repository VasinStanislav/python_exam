def func_1(x):
    if x[1] == 1984:
        return 13
    elif x[1] == 1993:
        return func_1_1(x)


def func_1_1(x):
    if x[0] == 1999:
        return 12
    elif x[0] == 2009:
        return 11
    elif x[0] == 1977:
        return func_1_1_1(x)


def func_1_1_1(x):
    if x[3] == 'IO':
        return 10
    elif x[3] == 'STON':
        return 9


def func_2(x):
    if x[0] == 1999:
        return 8
    elif x[0] == 2009:
        return 7
    elif x[0] == 1977:
        return 6


def func_3(x):
    if x[1] == 1984:
        return func_3_1(x)
    elif x[1] == 1993:
        return func_3_2(x)


def func_3_1(x):
    if x[3] == 'IO':
        return 5
    elif x[3] == 'STON':
        return 4


def func_3_2(x):
    if x[0] == 1999:
        return func_3_2_1(x)
    elif x[0] == 2009:
        return 1
    elif x[0] == 1977:
        return 0


def func_3_2_1(x):
    if x[3] == 'IO':
        return 3
    elif x[3] == 'STON':
        return 2


def main(x):
    value = -1

    if x[4] == 1984:
        value = func_1(x)
    elif x[4] == 1985:
        value = func_2(x)
    elif x[4] == 1987:
        value = func_3(x)

    return value


print(main([1999, 'IO', 1000, 1984, 2009]))
