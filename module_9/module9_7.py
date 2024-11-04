def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_prime_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Простое" if is_prime(result) else "Составное")
        return result

    return wrapper


@is_prime_decorator
def sum_three(a, b, c):
    """Сложение трех чисел."""
    return a + b + c

result = sum_three(2, 3, 6)
print(result)