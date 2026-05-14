# Лабораторна робота №7
# Тема: Робота з бінарним та червоно-чорним деревами пошуку
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Послідовність: 28, 76, 27, 10, 5, 35, 95, 16, 33
 
# ─── Бінарне дерево пошуку (BST) ─────────────────────────────────────────────
 
class Node:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None
 
 
def insert(root, key):
    """Вставка ключа в BST."""
    if root is None:
        return Node(key)
    if key < root.key:
        root.left  = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root
 
 
def min_node(node):
    """Мінімальний (крайній лівий) вузол піддерева."""
    while node.left:
        node = node.left
    return node
 
 
def delete(root, key):
    """Видалення вузла з BST."""
    if root is None:
        return root
    if key < root.key:
        root.left  = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left and root.right:
            # вузол має два нащадки: замінюємо мінімальним з правого піддерева
            m = min_node(root.right)
            root.key   = m.key
            root.right = delete(root.right, m.key)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None
    return root
 
 
# ─── Обходи ──────────────────────────────────────────────────────────────────
 
def inorder(node, result=None):
    """Симетричний обхід: ліво → корінь → право."""
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.key)
        inorder(node.right, result)
    return result
 
 
def preorder(node, result=None):
    """Прямий обхід: корінь → ліво → право."""
    if result is None:
        result = []
    if node:
        result.append(node.key)
        preorder(node.left, result)
        preorder(node.right, result)
    return result
 
 
def postorder(node, result=None):
    """Зворотний обхід: ліво → право → корінь."""
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.key)
    return result
 
 
def inorder_stack_trace(node):
    """Симетричний обхід із виведенням стану стека викликів."""
    call_stack = []
    step = [0]
 
    def helper(n):
        if n is None:
            return
        call_stack.append(n.key)
        step[0] += 1
        print(f"  {step[0]:>2}: стек = {call_stack}")
        helper(n.left)
        print(f"       → відвідуємо: {n.key}")
        helper(n.right)
        call_stack.pop()
 
    helper(node)
 
 
# ─── Головна програма ────────────────────────────────────────────────────────
 
def build_tree(keys):
    root = None
    for k in keys:
        root = insert(root, k)
    return root
 
 
if __name__ == "__main__":
    KEYS = [28, 76, 27, 10, 5, 35, 95, 16, 33]
    print("=" * 60)
    print(f" БІНАРНЕ ДЕРЕВО ПОШУКУ (BST)")
    print(f" Послідовність: {KEYS}")
    print("=" * 60)
 
    root = build_tree(KEYS)
 
    print(f"\n Inorder  (симетричний): {inorder(root)}")
    print(f" Preorder (прямий):      {preorder(root)}")
    print(f" Postorder(зворотний):   {postorder(root)}")
 
    print("\n Стек викликів симетричного обходу:")
    inorder_stack_trace(root)
 
    # ── Видалення ────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(" ВИДАЛЕННЯ ВУЗЛІВ З BST")
    print("=" * 60)
 
    r = build_tree(KEYS)
    print(f"\n  Початковий стан:      {inorder(r)}")
 
    # 1) Правий кореневий елемент = 76
    m = min_node(r.right)
    print(f"\n  Видаляємо праве піддерево (76):")
    print(f"    Мінімум правого піддерева 76 = {min_node(r.right).key} -> замінює 76")
    r = delete(r, 76)
    print(f"    Результат: {inorder(r)}")
 
    # 2) Лівий кореневий елемент = 27
    print(f"\n  Видаляємо ліве піддерево (27):")
    if r.left and r.left.right:
        print(f"    Мінімум правого піддерева 27 = {min_node(r.left.right).key} -> замінює 27")
    else:
        print(f"    Вузол 27 має лише лівого нащадка — замінюємо ним")
    r = delete(r, 27)
    print(f"    Результат: {inorder(r)}")
 
    # 3) Кореневий елемент = 28
    print(f"\n  Видаляємо корінь (28):")
    m2 = min_node(r.right)
    print(f"    Мінімум правого піддерева = {m2.key} -> замінює 28")
    r = delete(r, 28)
    print(f"    Результат: {inorder(r)}")
