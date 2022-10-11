def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    for i in range(0, 10):
        print(fibonacci(i))

    # a = lambda x: x*2
    # print(a(8))


if __name__ == '__main__':
    main()
