import logging
from tournament import Tournament  # Предполагается, что класс Tournament находится в файле tournament.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='tournament_tests.log',
    filemode='w',
    encoding='UTF-8'
)

class TournamentTest:

    def test_register(self):
        try:
            # Попытка создать объект Tournament с отрицательным значением для distance
            Tournament(distance=-100)
            logging.info('"test_register" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверное значение для Tournament")

    def test_start(self):
        try:
            # Попытка создать объект Tournament с неверным типом данных для distance
            Tournament(distance="100")
            logging.info('"test_start" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Tournament")

# Пример использования
if __name__ == "__main__":
    tester = TournamentTest()
    tester.test_register()
    tester.test_start()