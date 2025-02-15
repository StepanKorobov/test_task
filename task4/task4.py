import os
import sys

# Путь к файлу с заданием (нужен для создания пути к файлу)
# Предполагается, что файлы будут находиться в папке с заданием либо во вложенной папке
project_path = os.path.dirname(os.path.abspath(__file__))


def get_move_count_nums(nums):
    average = int(sum(nums) / len(nums))
    # count = sum(abs(num - average) for num in nums)

    # Если нужно нужно привести все элементы к среднему из списка
    # Используем медиану списка
    # nums.sort()
    # average = nums[len(nums) // 2]

    move_count = 0

    for i_num in range(len(nums)):
        while nums[i_num] != average:
            if nums[i_num] > average:
                nums[i_num] -= 1
                move_count += 1
            elif nums[i_num] < average:
                nums[i_num] += 1
                move_count += 1

    return nums, move_count


def get_move_count(nums):
    average = int(sum(nums) / len(nums))
    # Если нужно нужно привести все элементы к среднему из списка
    # Используем медиану списка
    # nums.sort()
    # average = nums[len(nums) // 2]

    count = sum([abs(i_num - average) for i_num in nums])

    return count


if __name__ == "__main__":
    # Пример запуска программы: python .\task4.py numbers.txt

    path = sys.argv[1]

    path_file = os.path.join(project_path, path)

    with open(path_file, "r") as f:
        nums = [int(i) for i in f]

    # Функция создаёт новый список и считает количество ходов
    # result = get_move_count_nums(nums.copy())
    # print(f"Изначальный список: {nums}, получившийся список: {result[0]}, количество ходов: {result[1]}")

    # Функция считает количество ходов
    # работает быстрее, так как не надо создавать список и менять в нём значения
    result = get_move_count(nums)
    print(result)
