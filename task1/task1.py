import sys
from typing import Tuple


def get_result_interval_and_paths(n, m) -> Tuple[str, str]:
    """
    Функция создающая путь по которому двигается интервал длины
    """

    # Создаём список из чисел от 1 до n
    numbers_list: list = [i for i in range(1, n + 1)]
    # Текущий индекс, начинаем с нуля
    current_index: int = 0
    # Лист содержащий первые элементы интервалов
    intervals_list: list = list()
    # Список содержащий интервалы
    paths_list: list = list()

    # Используем цикл While, так как заранее не знаем сколько итераций потребуется
    while True:
        # Список интервала
        new_list: list = list()
        # Индекс, по которому будем создавать список интервала
        cur_index = current_index
        for i in range(m):
            # Обновляем индекс
            curr_index: int = (cur_index + i) % len(numbers_list)
            # Добавляем элемент в список интервалов
            new_list.append(str(numbers_list[curr_index]))

        paths_list.append("".join(new_list))

        # Добавляем элемент по индексу (получается первый элемент интервала)
        intervals_list.append(str(numbers_list[current_index]))
        # Вычисляем индекс первого элемента следующего интервала
        current_index: int = (current_index + m - 1) % n
        # Если индекс следующего элемента 0, то прерываем цикл
        if current_index == 0:
            break

    intervals = "".join(intervals_list)
    paths = ",".join(paths_list)

    return intervals, paths


def get_result_interval(n, m) -> str:
    """
    Функция создающая путь по которому двигается интервал длины
    """

    # Создаём список из чисел от 1 до n
    numbers_list: list = [i for i in range(1, n + 1)]
    # Текущий индекс, начинаем с нуля
    current_index: int = 0
    # Лист содержащий первые элементы интервалов
    intervals_list: list = list()

    # Используем цикл While, так как заранее не знаем точно сколько итераций потребуется
    while True:
        # Добавляем элемент по индексу (получается первый элемент интервала)
        intervals_list.append(str(numbers_list[current_index]))
        # Вычисляем индекс первого элемента следующего интервала
        current_index: int = (current_index + m - 1) % n
        # Если индекс следующего элемента 0, то прерываем цикл
        if current_index == 0:
            break

    intervals: str = "".join(intervals_list)

    return intervals


if __name__ == "__main__":
    # Пример запуска программы: python task1.py 5 4
    n: int = int(sys.argv[1])
    m: int = int(sys.argv[2])

    # Первый вариант выводит только список путей, сложность получилась O(n)
    result = get_result_interval(n, m)
    print(result)

    # Второй вариант выводит список путей и интервалы, сложность получилась O(n*n)
    # result = get_result_interval_and_paths(n, m)
    # print(f"Интервалы: {result[0]}, Полученный путь: {result[1]}")
