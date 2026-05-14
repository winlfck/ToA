# Лабораторна робота №2
# Тема: Логарифмічні алгоритми сортування
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Послідовність: 69, 52, 97, 27, 10, 88, 29, 1, 24
 
def partition(a, l, r):
    comparisons = 0
    assignments = 0
 
    pivot = a[l]
    assignments += 1
    i = l - 1
    j = r + 1
    assignments += 2
 
    print(f"  Вибираємо опорний елемент (pivot): {pivot}")
 
    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1  # вихід з внутрішнього while
 
        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1  # вихід з внутрішнього while
 
        comparisons += 1
        if i >= j:
            print(f"  Індекси перетнулися. Поділ завершено. Повертаємо j={j}.")
            return j, comparisons, assignments
 
        print(f"  Поточні індекси: i={i}, j={j}. Обмінюємо a[{i}] ({a[i]}) і a[{j}] ({a[j]}). Масив: ", end="")
        a[i], a[j] = a[j], a[i]
        assignments += 3
        print(a)
 
 
def quicksort(a, l, r, depth=0):
    indent = "  " * depth
    comparisons = 0
    assignments = 0
    recursive_calls = 1
 
    print(f"{indent}Quicksort виклик: масив = {a}, l = {l}, r = {r}")
 
    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
 
        c2, a2, r2 = quicksort(a, l, q, depth + 1)
        c3, a3, r3 = quicksort(a, q + 1, r, depth + 1)
 
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0
 
    return comparisons, assignments, recursive_calls
 
 
# Варіант 8
my_list = [69, 52, 97, 27, 10, 88, 29, 1, 24]
print("--- ШВИДКЕ СОРТУВАННЯ (схема Хоара) ---")
print(f"Початковий масив: {my_list}\n")
 
total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)
 
print(f"\nВідсортований масив: {my_list}")
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")
