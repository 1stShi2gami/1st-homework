import unittest
import logging
from module12.module12_1 import Runner


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format='%(levelname)s | %(message)s | %(asctime)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run_1 = Runner('John', -5)
            for i in range(10):
                run_1.walk()
            logging.info(f'"test_walk" выполнен успешно')
            self.assertEqual(run_1.distance, 50)
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run_2 = Runner(10, 10)
            for i in range(10):
                run_2.run()
                logging.info(f'"test_run" выполнен успешно')
                self.assertEqual(run_2.distance, 100)
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)



if __name__ == '__main__':
    unittest.main()