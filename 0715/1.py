input_type = ['NTD', 'GBP', 'KRW', 'USD', 'JPY']
coin_value = {'NTD': 37.7412, 'KRW': 1526.73, 'USD': 1.2588, 'JPY': 134.99}


def check_input(s, is_x):
    if is_x and s == 'end':
        return False
    for i in input_type:
        if s == i:
            return True
    print('ERROR!! Input again!!')
    return False


def exchange(x, n, y):
    if x != input_type[1]:
        n /= coin_value[x]
    return n*coin_value[y]


while True:
    x = input()
    is_end = False
    while not check_input(x, True):
        if x == 'end':
            is_end = True
            break
        x = input()
    if is_end:
        break

    n = float(input())
    while n < 0:
        print('N cannot smaller than 0!! Input again!!')
        n = float(input())

    y = input()
    while not check_input(y, False):
        y = input()

    print(f'{n} {x} = {exchange(x,n,y):.3f} {y}')
