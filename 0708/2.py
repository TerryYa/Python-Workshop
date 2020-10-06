def main():
    while(1):
        n = int(input())
        sum = 0
        if n == 0:
            break
        for i in range(1, n+1):
            sum += pow(i, i)
        print(str(sum)[-1])


if __name__ == "__main__":
    main()
