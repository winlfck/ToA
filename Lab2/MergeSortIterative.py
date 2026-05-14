# Лабораторна робота №2
# Тема: Логарифмічні алгоритми сортування
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Послідовність: 69, 52, 97, 27, 10, 88, 29, 1, 24
 
def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
 
    L = a[left:mid]
    R = a[mid:right]
    assignments += len(L) + len(R)
 
    it1 = 0
    it2 = 0
    k = left
    assignments += 3  # it1, it2, k
 
    print(f"  Об'єднуємо підмасиви: a[{left}:{mid}] ({L}) і a[{mid}:{right}] ({R})")
 
    while it1 < len(L) and it2 < len(R):
        comparisons += 1
        if L[it1] < R[it2]:
            print(f"    Порівняння: {L[it1]} < {R[it2]} -> True. Беремо {L[it1]}")
            a[k] = L[it1]
            it1 += 1
            assignments += 1
        else:
            print(f"    Порівняння: {L[it1]} < {R[it2]} -> False. Беремо {R[it2]}")
            a[k] = R[it2]
            it2 += 1
            assignments += 1
        k += 1
        assignments += 1
 
    while it1 < len(L):
        a[k] = L[it1]
        print(f"    Додаємо залишок з лівого: {L[it1]}")
        it1 += 1
        k += 1
        assignments += 1
 
    while it2 < len(R):
        a[k] = R[it2]
        print(f"    Додаємо залишок з правого: {R[it2]}")
        it2 += 1
        k += 1
        assignments += 1
 
    print(f"  Масив після об'єднання: {a}")
    print("-" * 50)
 
    return comparisons, assignments
 
 
def merge_sort_iterative(a):
    n = len(a)
    total_comparisons = 0
    total_assignments = 0
 
    i = 1
    pass_num = 1
    while i < n:
        print(f"\nПРОХІД size={i} (pass {pass_num})")
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            c, a_count = merge(a, left, mid, right)
            total_comparisons += c
            total_assignments += a_count
            j += 2 * i
        print(f"Після проходу size={i}: {a}")
        i *= 2
        pass_num += 1
 
    return a, total_comparisons, total_assignments
 
 
# Варіант 8
my_list = [69, 52, 97, 27, 10, 88, 29, 1, 24]
print("--- ІТЕРАТИВНА ВЕРСІЯ СОРТУВАННЯ ЗЛИТТЯМ ---")
print(f"Початковий масив: {my_list}")
print("-" * 50)
 
sorted_list, comps, assigns = merge_sort_iterative(my_list.copy())
 
print(f"\nВідсортований масив: {sorted_list}")
print(f"Загальна кількість порівнянь: {comps}")
print(f"Загальна кількість присвоювань: {assigns}")
