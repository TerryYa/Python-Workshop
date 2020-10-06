import numpy as np


def get_arr():
    n, m = [int(i) for i in input().split()]
    arr = np.zeros((n, m)).astype(np.int)
    for i in range(n):
        arr[i] = np.array([int(j) for j in input().split()])
    return arr


def main():
    arr = get_arr()
    while True:
        mode = int(input('request: '))
        if mode == 4:
            print(arr)
        elif mode == 3:
            arr = arr.T
        else:
            if mode == 2:
                try:
                    arr = arr.dot(get_arr())
                except ValueError:
                    print('fail')
            elif mode == 1:
                n, m = [int(i) for i in input().split()]
                arr = arr.reshape((n, m))
            else:
                break


if __name__ == "__main__":
    main()
