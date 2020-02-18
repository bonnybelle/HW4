# 2. Дан массив целых чисел. Нужно найти сумму элементов с индексами подходящими под правило.
# Правило такое - сумма бит двоичного представления четна.
# Затем перемножить эту сумму и предпоследний элемент исходного массива.

array = [int(i) for i in input('Введите массив: ').split(' ')]


def to_bin(array):
    elements = []
    f = array[-2]
    for x in range(len(array)):
        x1 = x
        x = str(bin(x)[2:])
        sum_bit = sum(int(i) for i in x.split())
        if sum_bit % 2 == 0 and sum_bit != 0:
            elements.append(array[x1])
    sum_elements = sum(elements)
    result = sum_elements * f
    print('Элементы с правильными индексами:', elements, '\nСумма этих элементов:', sum_elements, '\nИтог:', result)


to_bin(array)
