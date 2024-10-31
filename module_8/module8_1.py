def add_everything_up(a, b):
    try:
        if type(a) != type(b):
            return str(a) + str(b)

    except TypeError:
        return 'Невозможно сложить эти данные'

    finally:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return round(a + b, 3)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))