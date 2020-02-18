# 1. Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами.
# Функция должна иметь вид: def swap(target_list, item_index1, item_index2).

target_list = [int(i) for i in input('Введите массив: ').split(' ')]
item_index1 = int(input('Индекс элемета №1: '))
item_index2 = int(input('Индекс элемета №2: '))


def swap(target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]
    print(target_list)


swap(target_list, item_index1, item_index2)
