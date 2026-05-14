# Лабораторна робота №2
# Тема: Логарифмічні алгоритми сортування
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Послідовність: 69, 52, 97, 27, 10, 88, 29, 1, 24
 
def merge(left, right, depth):
    merged = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    indent = "  " * depth
 
    print(f"{indent}Зливаємо {left} та {right}")
 
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            print(f"{indent}  Порівняння: {left[i]} <= {right[j]} -> True. Додаємо {left[i]}")
            merged.append(left[i])
            i += 1
        else:
            print(f"{indent}  Порівняння: {left[i]} <= {right[j]} -> False. Додаємо {right[j]}")
            merged.append(right[j])
            j += 1
        assignments += 1
 
    while i < len(left):
        print(f"{indent}  Додаємо залишок з лівого масиву: {left[i]}")
        merged.append(left[i])
        i += 1
        assignments += 1
 
    while j < len(right):
        print(f"{indent}  Додаємо залишок з правого масиву: {right[j]}")
        merged.append(right[j])
        j += 1
        assignments += 1
 
    print(f"{indent}Злиття завершено. Результат: {merged}")
    return merged, comparisons, assignments
 
 
def merge_sort_recursive(arr, depth=0):
    indent = "  " * depth
    comparisons = 0
    assignments = 0
    recursive_calls = 1
 
    print(f"{indent}Розділяємо масив: {arr}")
 
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
 
    mid = len(arr) // 2
    assignments += 1
 
    left_half = arr[:mid]
    right_half = arr[mid:]
 
    sorted_left, c1, a1, r1 = merge_sort_recursive(left_half, depth + 1)
    sorted_right, c2, a2, r2 = merge_sort_recursive(right_half, depth + 1)
 
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
 
    merged, c_merge, a_merge = merge(sorted_left, sorted_right, depth + 1)
    comparisons += c_merge
    assignments += a_merge
 
    return merged, comparisons, assignments, recursive_calls
 
 
# Варіант 8
my_list = [69, 52, 97, 27, 10, 88, 29, 1, 24]
print("--- РЕКУРСИВНА ВЕРСІЯ СОРТУВАННЯ ЗЛИТТЯМ ---")
print(f"Початковий масив: {my_list}\n")
 
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
 
print(f"\nФінальний відсортований масив: {sorted_list}")
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
