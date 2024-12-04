import asyncio

async def start_tournament():
    # Список участников силачей
    strongmen = [('Тим', 3), ('Ник', 4), ('Лёха', 5)]

    # Создаем список задач для каждого силача
    tasks = [start_strongman(name, power) for name, power in strongmen]

    # Запускаем все задачи одновременно
    await asyncio.gather(*tasks)

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    # Имитация подъема шаров Атласа
    for ball in range(1, 6):
        print(f'Силач {name} поднял шар {ball}.')
        await asyncio.sleep(5 / power)  # Задержка пропорциональна силе силача.

    print(f'Силач {name} закончил соревнования.')

# старт
asyncio.run(start_tournament())