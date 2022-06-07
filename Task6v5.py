def func2_2(x):
    if x[1] == 'COQ':
        return 2
    if x[1] == 'ROFF':
        return 1
    if x[1] == 'JSX':
        return 0


def func2_1(x):
    if x[1] == 'COQ':
        return 5
    if x[1] == 'ROFF':
        return 4
    if x[1] == 'JSX':
        return 3


def func_1_2(x):
    if x[3] == 2015:
        return 6
    if x[3] == 1980:
        return 7


def func_1_1(x):
    if x[3] == 2015:
        return 8
    if x[3] == 1980:
        return 9


def func_2(x):
    if x[3] == 1980:
        return func2_1(x)
    if x[3] == 2015:
        return func2_2(x)


def func_1(x):
    if x[1] == 'COQ':
        return 10
    if x[1] == 'ROFF':
        return func_1_1(x)
    if x[1] == 'JSX':
        return func_1_2(x)


def main(x):
    if x[2] == 2013:
        return func_1(x)
    if x[2] == 1991:
        return func_2(x)


print(main([1957, 'JSX', 1991, 1980]))
