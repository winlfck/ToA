# Лабораторна робота №4
# Тема: Робота з хеш-таблицями
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Прислів'я: "Хто людям добра бажає, той і собі має"
 
import math
 
# ─── Вхідні дані ────────────────────────────────────────────────────────────
WORDS = ["Хто", "людям", "добра", "бажає", "той", "і", "собі", "має"]
 
M_DIV = 13   # розмір таблиці для методу ділення
M_MUL = 16   # розмір таблиці для методу множення
A = (5 ** 0.5 - 1) / 2  # константа Кнута ≈ 0.6180339887
 
# Позиції українських букв
UA_POS = {
    'А': 1,  'Б': 2,  'В': 3,  'Г': 4,  'Ґ': 5,  'Д': 6,  'Е': 7,
    'Є': 8,  'Ж': 9,  'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14,
    'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21,
    'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}
 
 
# ─── Хеш-функції ────────────────────────────────────────────────────────────
def letter_sum(word: str) -> int:
    """Сума позицій букв слова в українському алфавіті."""
    return sum(UA_POS.get(c.upper(), 0) for c in word)
 
 
def hash_division(word: str, m: int = M_DIV) -> int:
    """Метод ділення: h(k) = sum mod m."""
    return letter_sum(word) % m
 
 
def hash_multiplication(word: str, m: int = M_MUL) -> int:
    """Метод множення: h(k) = floor(m * (sum*A mod 1)), A = (√5-1)/2."""
    s = letter_sum(word)
    return math.floor(m * ((s * A) % 1))
 
 
# ─── Відкрита хеш-таблиця (хешування з ланцюжками) ─────────────────────────
def build_open_hash_table(words: list, hash_func) -> list:
    """Будує хеш-таблицю з роздільними ланцюжками."""
    m = M_DIV if hash_func == hash_division else M_MUL
    table = [[] for _ in range(m)]
    for word in words:
        h = hash_func(word)
        table[h].append(word)
        print(f"  INSERT '{word}': сума={letter_sum(word)}, h={h} -> [{h}]: {table[h]}")
    return table
 
 
def display_open_table(table: list, title: str):
    """Виводить відкриту хеш-таблицю."""
    print(f"\n{'─'*50}")
    print(f" {title}")
    print(f"{'─'*50}")
    for i, chain in enumerate(table):
        content = " -> ".join(chain) if chain else "(порожньо)"
        print(f"  [{i:02d}]: {content}")
 
 
def search_open(table: list, key: str, hash_func) -> int:
    """Пошук у відкритій хеш-таблиці. Повертає кількість порівнянь."""
    h = hash_func(key)
    chain = table[h]
    comparisons = 0
    for item in chain:
        comparisons += 1
        if item == key:
            print(f"  Пошук '{key}': h={h}, знайдено за {comparisons} порівнянь")
            return comparisons
    print(f"  Пошук '{key}': h={h}, не знайдено ({comparisons} порівнянь)")
    return comparisons
 
 
# ─── Закрита хеш-таблиця (відкрита адресація, лінійне зондування) ───────────
def build_closed_hash_table(words: list, hash_func) -> list:
    """Будує хеш-таблицю з відкритою адресацією (лінійне зондування)."""
    m = M_DIV if hash_func == hash_division else M_MUL
    table = [None] * m
    for word in words:
        h0 = hash_func(word)
        for i in range(m):
            h = (h0 + i) % m
            if table[h] is None:
                table[h] = word
                if i == 0:
                    print(f"  INSERT '{word}': h={h0}, розміщено у [{h}]")
                else:
                    print(f"  INSERT '{word}': h={h0} -> КОЛІЗІЯ -> розміщено у [{h}] (крок {i})")
                break
        else:
            print(f"  ПОМИЛКА: таблиця повна, '{word}' не вставлено")
    return table
 
 
def display_closed_table(table: list, title: str):
    """Виводить закриту хеш-таблицю."""
    print(f"\n{'─'*50}")
    print(f" {title}")
    print(f"{'─'*50}")
    for i, item in enumerate(table):
        print(f"  [{i:02d}]: {item if item is not None else '(NULL)'}")
 
 
def search_closed(table: list, key: str, hash_func) -> int:
    """Пошук у закритій хеш-таблиці. Повертає кількість порівнянь."""
    m = len(table)
    h0 = hash_func(key)
    comparisons = 0
    for i in range(m):
        h = (h0 + i) % m
        if table[h] is None:
            print(f"  Пошук '{key}': не знайдено ({comparisons} порівнянь)")
            return comparisons
        comparisons += 1
        if table[h] == key:
            print(f"  Пошук '{key}': знайдено у [{h}] за {comparisons} порівнянь")
            return comparisons
    print(f"  Пошук '{key}': не знайдено після перегляду всієї таблиці")
    return comparisons
 
 
# ─── Аналіз ефективності пошуку ─────────────────────────────────────────────
def analyze_search(table, words, hash_func, table_type="open"):
    """Підраховує порівняння при пошуку всіх елементів."""
    print(f"\n  Аналіз пошуку ({table_type}):")
    total = 0
    max_cmp = 0
    max_word = ""
    for word in words:
        if table_type == "open":
            cmp = search_open(table, word, hash_func)
        else:
            cmp = search_closed(table, word, hash_func)
        total += cmp
        if cmp > max_cmp:
            max_cmp = cmp
            max_word = word
    avg = total / len(words)
    print(f"\n  Максимум порівнянь: '{max_word}' — {max_cmp}")
    print(f"  Середня кількість порівнянь: {avg:.2f}")
 
 
# ─── Головна програма ────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print(" ЛАБОРАТОРНА РОБОТА №4 — Хеш-таблиці")
    print(f" Прислів'я: «{'  '.join(WORDS)}»")
    print("=" * 60)
 
    print("\n[1] Суми позицій та хеш-значення:")
    print(f"  {'Слово':<10} {'Сума':>6}  {'h_div(m=13)':>12}  {'h_mul(m=16)':>12}")
    for w in WORDS:
        s = letter_sum(w)
        hd = hash_division(w)
        hm = hash_multiplication(w)
        print(f"  {w:<10} {s:>6}  {hd:>12}  {hm:>12}")
 
    # ── Метод ділення ──────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(" МЕТОД ДІЛЕННЯ h(k) = sum mod 13")
    print("=" * 60)
 
    print("\n[2a] Відкрита хеш-таблиця (ланцюжки), m=13:")
    open_div = build_open_hash_table(WORDS, hash_division)
    display_open_table(open_div, "Відкрита хеш-таблиця (ділення, m=13)")
    analyze_search(open_div, WORDS, hash_division, "open")
 
    print("\n[2b] Закрита хеш-таблиця (відкрита адресація), m=13:")
    closed_div = build_closed_hash_table(WORDS, hash_division)
    display_closed_table(closed_div, "Закрита хеш-таблиця (ділення, m=13)")
    analyze_search(closed_div, WORDS, hash_division, "closed")
 
    # ── Метод множення ─────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(" МЕТОД МНОЖЕННЯ h(k) = floor(16*(sum*A mod 1))")
    print("=" * 60)
 
    print("\n[3a] Відкрита хеш-таблиця (ланцюжки), m=16:")
    open_mul = build_open_hash_table(WORDS, hash_multiplication)
    display_open_table(open_mul, "Відкрита хеш-таблиця (множення, m=16)")
    analyze_search(open_mul, WORDS, hash_multiplication, "open")
 
    print("\n[3b] Закрита хеш-таблиця (відкрита адресація), m=16:")
    closed_mul = build_closed_hash_table(WORDS, hash_multiplication)
    display_closed_table(closed_mul, "Закрита хеш-таблиця (множення, m=16)")
    analyze_search(closed_mul, WORDS, hash_multiplication, "closed")
 
 
if __name__ == "__main__":
    main()
