import math


def task(array):
    str_lst = str(array)
    num_lst = []
    idx = None

    """"Создаем из массива список с типом данных int"""

    for el in str_lst:
        num_lst.append(int(el))

    """Создаем цикл перебора и проверки списка"""

    for el in num_lst:
        if el == 0:
            idx = num_lst.index(el)
            break
    return idx


print(task("111111111111111111111111100000000"))

'''Решение с использованием побитового поиска (значительно ускоряет поиск в огромных массивах)'''


def task1(array):
    str_lst = str(array)
    num_lst = []

    """"Создаем из массива список с типом данных int"""

    for el in str_lst:
        num_lst.append(int(el))

    """Создаем цикл перебора и проверки списка"""

    left_idx = 0
    right_idx = len(num_lst) - 1

    while left_idx != right_idx:
        mid_idx = math.ceil((right_idx - left_idx) / 2)
        if num_lst[right_idx - mid_idx] == 1:
            left_idx = left_idx + mid_idx
        elif num_lst[right_idx - mid_idx] == 0:
            right_idx = right_idx - mid_idx
    return left_idx


print(task1("111111111111111111111111100000000"))
