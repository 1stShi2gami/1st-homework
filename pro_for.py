def zip_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for a_val, b_val in zip(a, b):
        res = a_val + b_val  # Используем zip для объединения списков
    print(res)


print(zip_example())