import copy
import json
import os
import sys
from typing import Dict

# Путь к файлу с заданием (нужен для создания пути к файлу)
# Предполагается, что файлы будут находиться в папке с заданием либо во вложенной папке
project_path = os.path.dirname(os.path.abspath(__file__))


def data_parser(report_dict: dict, values_dict: dict) -> None:
    """
    Рекурсивная функция для подставления значений

    :param report_dict: Словарь в который подставляем значения
    :type report_dict: dict
    :param values_dict: Словарь со значениями
    :type values_dict: dict

    :return: Ничего не возвращает
    :rtype: None
    """

    # Если ключ id есть в словаре и данный есть в словаре со значениями
    if ("id" in report_dict) and (report_dict["id"] in values_dict):
        # Присваиваем новое значение
        report_dict["value"] = values_dict[report_dict["id"]]

    # Проходимся по данным
    for i_key, i_value in report_dict.items():
        # Если нашли список
        if isinstance(i_value, list):
            # Проходимся по списку
            for i_item in i_value:
                # Рекурсивно вызываем функцию передавая значения
                data_parser(i_item, values_dict)


def get_report(tests_path: str, values_path: str, report_path: str) -> None:
    """
    Функция считывающая файлы и записывающая результат

    :param tests_path: Путь к файлу с тестовыми данными
    :type tests_path: str
    :param values_path: Путь к файлу со значениями
    :type values_path: str
    :param report_path: Путь к файлу, в который записываем результат
    :type report_path: str

    :return: Ничего не возвращает
    :rtype: None
    """

    # Создаём путь к файлу с тестами
    tests_path = os.path.join(project_path, tests_path)
    # Создаём путь к файлу со значениями
    values_path = os.path.join(project_path, values_path)
    # Создаём путь к файлу с результатом
    report_path = os.path.join(project_path, report_path)

    # Читаем файл с тестами
    with open(tests_path, "r", encoding="utf-8") as f:
        tests_data = json.load(f)

    # Читаем файл со значениями
    with open(values_path, "r", encoding="utf-8") as f:
        values_data = json.load(f)

    # Так как в values_data нам известна вложенность и она не меняется
    # Создадим новый словарь со значениями для удобства поиска
    values_dict = {i_item["id"]: i_item["value"] for i_item in values_data["values"]}
    # Скопируем словарь с тестовыми данными (вдруг он нам ещё понадобится)
    report_data = copy.deepcopy(tests_data)
    # Вызываем рекурсивную функцию для подставления значений
    data_parser(report_data, values_dict)

    # Записываем значения
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    # Пример запуска программы: python task3.py tests.json values.json report.json

    # Путь к файлу с тестовыми данными
    tests_path: str = str(sys.argv[1])
    # Путь к файлу со значениями
    values_path: str = str(sys.argv[2])
    # Путь к файлу с решением
    report_path: str = str(sys.argv[3])

    # Вызываем функцию
    get_report(tests_path, values_path, report_path)
