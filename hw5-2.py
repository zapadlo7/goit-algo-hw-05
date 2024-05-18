def binary_search(arr, target):
    if len(arr) == 0:
        return 0, None

    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            upper_bound = mid_value
            return (iterations, upper_bound)
        elif mid_value < target:
            low = mid + 1
        else:
            upper_bound = mid_value
            high = mid - 1

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]
    
    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

# Вивід результатів тестування
for target in [3.5, 4.6, 5.9]: 
    print(binary_search(arr, target))
