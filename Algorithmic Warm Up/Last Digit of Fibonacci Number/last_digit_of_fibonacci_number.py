# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10

def fib(f, n):
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10

    return f

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    f = [0] * 61

    # Precomputing units digit of
    # first 60 Fibonacci numbers
    f = fib(f, 60)

    return f[n % 60]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
