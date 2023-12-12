def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Элемент найден, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится справа от центра
        else:
            right = mid - 1  # Искомый элемент находится слева от центра

    return -1  # Искомый элемент не найден

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

# Вывод результата
print(f'Искомый элемент {target} находится по индексу: {result}')
