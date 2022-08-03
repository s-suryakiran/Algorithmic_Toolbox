# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    def calculateRange(m):
        previous, current = 0,1
        for i in range(m*m):
            previous, current = current, (previous+current) % m
            if previous == 0 and current == 1:
                return i + 1

    frange = calculateRange(m)
    n = n % frange
    if n == 0 or n == 1:
        return n
    previous = 0
    current = 1
    for i in range(n-1):
        previous, current = current, (previous+current)

    return current % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
