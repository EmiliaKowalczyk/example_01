def sum(a, b):
    return a + b


def multiply(a, b, c):
    return a * b * c


# TODO: example with args and kwargs

def main(a, b):
    print(f'multiplication: 3 + 3 = {multiply(a, b,c)}')
    print(f'Sum: 3 + 3 = {sum(a, b)}')

if __name__ == '__main__':
    try:
        a, b, c = '3', 3, 4
        main(a, b, c)
    except TypeError as err:
        print(err)
        a, b, c = 3, 3, 4
        main(a, b, c)