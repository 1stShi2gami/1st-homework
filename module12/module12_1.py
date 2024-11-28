import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('walker')
        for _ in range(10):  # Создаем объект класса Runner
            runner.walk()  # Вызываем метод walk 10 раз
        self.assertEqual(runner.distance, 50)  # Сравниваем свойство distance с 50

    def test_run(self):
        runner = Runner('runner')
        for _ in range(10):  # Создаем объект класса Runner
            runner.run()  # Вызываем метод run 10 раз
        self.assertEqual(runner.distance, 100)  # Сравниваем свойство distance с 100

    def test_challenge(self):
        runner = Runner('walker')
        runner_2 = Runner('runner')
        for _ in range(10):  # Создаем объекты класса Runner
            runner.walk()
            runner_2.run()
        self.assertNotEqual(runner.distance, runner_2.distance)  # Сравниваем свойство distance

if __name__ == '__main__':
    unittest.main()