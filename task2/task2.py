import os
import sys
from typing import Tuple

# Путь к файлу с заданием (нужен для создания пути к файлу)
# Предполагается, что файлы будут находиться в папке с заданием либо во вложенной папке
project_path = os.path.dirname(os.path.abspath(__file__))


def read_file_circle(path_to_circle: str) -> Tuple[Tuple[float], float]:
    """
    Функция читающая файл с координатами окружности и её радиусом

    :param path_to_circle: Путь к файлу с данными об окружности
    :type path_to_circle: str
    :return: Возвращает кортеж с данными о координатах и радиусе
    :rtype: Tuple[Tuple[float], float]
    """

    # Создаём пусть к файлу в котором содержится информация о положении и радиусе окружности
    path: str = os.path.join(project_path, path_to_circle)
    # Читаем файл
    with open(path, "r") as f:
        # Координаты окружности
        circle_center_x_y: tuple = tuple(
            [float(i_coordinate) for i_coordinate in f.readline().split()]
        )
        # Радиус окружности
        radius = float(f.readline())

    return circle_center_x_y, radius


def read_file_dor(path_to_dod: str) -> Tuple[Tuple[float, float]]:
    """
    Функция читающая файл с координатами окружности и её радиусом

    :param path_to_dod: Путь к файлу с данными о точках
    :type path_to_dod: str
    :return: Возвращает кортеж с кортежами, в которых содержатся координаты точек
    :rtype: Tuple[Tuple[float, float]]
    """

    # Создаём пусть к файлу в котором содержится информация о координатах точек
    path: str = os.path.join(project_path, path_to_dod)
    # Создаём список для будущих точек
    dots_list: list = list()

    # Читаем файл
    with open(path, "r") as f:
        for i_line in f:
            # Координаты точки
            dots = tuple([float(i_coordinate) for i_coordinate in i_line.split()])
            # Добавляем координаты в список
            dots_list.append(dots)

    # Преобразуем список в кортеж
    dots_tuple: tuple = tuple(dots_list)

    return dots_tuple


def get_poit_position(
    circle_coordinate: Tuple[float, float],
    circle_radius: float,
    dot_coordinate: Tuple[float, float],
) -> int:
    """
    Функция определяющая положение точки на окружности

    :param circle_coordinate: Кортеж с координатами окружности
    :type circle_coordinate: Tuple[float, float]
    :param circle_radius: Радиус окружности
    :type circle_radius: float
    :param dot_coordinate: Кортеж с координатами точек
    :type dot_coordinate: Tuple[float, float]
    :return: Возвращает информацию о положении точки на окружности
    :rtype: int
    """

    # Вычисляем расстояние между центром окружности и точкой
    distance_squared = (dot_coordinate[0] - circle_coordinate[0]) ** 2 + (
        dot_coordinate[1] - circle_coordinate[1]
    ) ** 2
    # Возводим окружность в квадрат
    radius_squared = circle_radius**2

    # Если расстояние меньше окружности
    if distance_squared < radius_squared:
        return 1
    # Если расстояние и окружность совпадают
    elif distance_squared == radius_squared:
        return 0
    # Если расстояние больше окружности
    else:
        return 2


def determine_position_points(
    circle_coordinate: Tuple[float, float],
    circle_radius: float,
    dot_coordinate: Tuple[Tuple[float, float]],
) -> None:
    """
    Функция нахождения положения всех точек на окружности

    :param circle_coordinate: Кортеж с координатами окружности
    :type circle_coordinate: Tuple[float, float]
    :param circle_radius: Радиус окружности
    :type circle_radius: float
    :param dot_coordinate: Кортеж с кортежами содержащим координатамы точек
    :type dot_coordinate: Tuple[Tuple[float, float]]
    :return: Ничего не возвращает
    :rtype: None
    """

    # В цикле проходимся по всем координатам точек
    for i_coordinate in dot_coordinate:
        # Получаем позицию
        position = get_poit_position(circle_coordinate, circle_radius, i_coordinate)
        print(position)


if __name__ == "__main__":
    # Пример запуска программы: python task2.py circle.txt dot.txt

    # Путь к файлу с информацией об окружности
    circle_path = sys.argv[1]
    # Путь к файлу с информацией о точках
    dod_path = sys.argv[2]

    # Получаем информацию из прочтённого файла
    circle_data: tuple = read_file_circle(circle_path)
    # Получаем информацию из прочтённого файла
    dot_data: tuple = read_file_dor(dod_path)

    determine_position_points(circle_data[0], circle_data[1], dot_data)
