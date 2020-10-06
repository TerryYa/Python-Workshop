def main():
    while True:
        n = int(input())
        if n == 0:
            break

        arr, cnt = [], 0
        for i in range(n):
            arr.append(int(input()))

        for i in range(n):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
