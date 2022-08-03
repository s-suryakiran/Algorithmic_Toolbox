# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n >= 2:
        a = [None] * (n+1)
        a[0] = 0
        a[1] = 1
        for i in range(2,n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]
    else:
        if n == 0:
            return 0
        else:
            return 1


if __name__ == '__main__':
    input_n = int(input())

    print(fibonacci_number(input_n))
