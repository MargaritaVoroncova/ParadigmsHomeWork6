# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Искомый элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится в правой половине
        else:
            right = mid - 1  # Искомый элемент находится в левой половине

    return -1  # Элемент не найден


# Вводим массив с клавиатуры
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Запрашиваем  число у пользователя
try:
    target = int(input("Введите  число: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit(1)

result = binary_search(arr, target)

if result != -1:
    print(f" число{target} найдено в массиве по индексу {result}.")
else:
    print(f" число {target} не найдено в массиве.")
