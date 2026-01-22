def sum(a, b):
    return a + b


def multiply(a, b, c):
    return a * b * c


# TODO: example with args and kwargs

def main(a, b):
    print(f'multiplication: {a} * {b} = {multiply(a, b)}')
    print(f'Sum: {a} + {b} = {sum(a, b)}')


try:
    a, b = '3', 3
    main(a, b)
except TypeError as err:
    print(err)
    a, b = 3, 3
    main(a, b)
