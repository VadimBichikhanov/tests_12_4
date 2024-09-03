import logging
from runner import Runner  # Предполагается, что класс Runner находится в файле runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8'
)

class RunnerTest:

    def test_walk(self):
        try:
            # Попытка создать объект Runner с отрицательной скоростью
            runner = Runner(name="John", speed=-1)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            # Попытка создать объект Runner с неверным типом данных для name
            runner = Runner(name=123, speed=10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")

# Пример использования
if __name__ == "__main__":
    tester = RunnerTest()
    tester.test_walk()
    tester.test_run()