def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by Zero")
    return a / b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    return a**0.5


def power(base, exponent):
    return base**exponent


def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
