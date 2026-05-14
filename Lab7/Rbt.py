# Лабораторна робота №7
# Тема: Робота з бінарним та червоно-чорним деревами пошуку
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Послідовність: 28, 76, 27, 10, 5, 35, 95, 16, 33
 
# ─── Червоно-чорне дерево (RBT) ──────────────────────────────────────────────
 
RED   = "RED"
BLACK = "BLACK"
 
 
class RBNode:
    def __init__(self, key):
        self.key    = key
        self.color  = RED
        self.left   = None
        self.right  = None
        self.parent = None
 
    def __repr__(self):
        c = "R" if self.color == RED else "B"
        return f"{self.key}({c})"
 
 
class RBTree:
    def __init__(self):
        # NIL-sentinel (чорний)
        self.NIL  = RBNode(0)
        self.NIL.color = BLACK
        self.root = self.NIL
 
    # ── Повороти ─────────────────────────────────────────────────────────────
 
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left   = x
        x.parent = y
 
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right  = x
        x.parent = y
 
    # ── Вставка ──────────────────────────────────────────────────────────────
 
    def insert(self, key):
        z = RBNode(key)
        z.left  = self.NIL
        z.right = self.NIL
 
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
 
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
 
        z.color = RED
        self._fix_insert(z)
 
    def _fix_insert(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right          # дядько
                if y.color == RED:                 # Випадок 1
                    z.parent.color         = BLACK
                    y.color                = BLACK
                    z.parent.parent.color  = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:        # Випадок 3 -> 2
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color        = BLACK  # Випадок 2
                    z.parent.parent.color = RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color        = BLACK
                    y.color               = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color        = BLACK
                    z.parent.parent.color = RED
                    self._left_rotate(z.parent.parent)
        self.root.color = BLACK
 
    # ── Обходи ───────────────────────────────────────────────────────────────
 
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
 
    def _inorder(self, node, result):
        if node != self.NIL:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
 
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
 
    def _preorder(self, node, result):
        if node != self.NIL:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
 
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
 
    def _postorder(self, node, result):
        if node != self.NIL:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)
 
    def inorder_stack_trace(self):
        """Симетричний обхід із виведенням стану стека викликів."""
        call_stack = []
        step = [0]
 
        def helper(n):
            if n == self.NIL:
                return
            call_stack.append(repr(n))
            step[0] += 1
            print(f"  {step[0]:>2}: стек = {list(call_stack)}")
            helper(n.left)
            print(f"       → відвідуємо: {repr(n)}")
            helper(n.right)
            call_stack.pop()
 
        helper(self.root)
 
    def height(self):
        def h(n):
            if n == self.NIL: return 0
            return 1 + max(h(n.left), h(n.right))
        return h(self.root)
 
    def black_height(self):
        node = self.root
        bh = 0
        while node != self.NIL:
            if node.color == BLACK:
                bh += 1
            node = node.left
        return bh
 
    # ── Видалення ────────────────────────────────────────────────────────────
 
    def delete(self, key):
        z = self._search(self.root, key)
        if z == self.NIL:
            print(f"  Ключ {key} не знайдено")
            return
        self._delete_node(z)
 
    def _search(self, node, key):
        while node != self.NIL and node.key != key:
            node = node.left if key < node.key else node.right
        return node
 
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
 
    def _delete_node(self, z):
        y = z
        y_orig_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_orig_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_orig_color == BLACK:
            self._fix_delete(x)
 
    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
 
    def _fix_delete(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:                         # Випадок 4
                    w.color         = BLACK
                    x.parent.color  = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:  # Випадок 5
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:             # Випадок 3
                        w.left.color = BLACK
                        w.color      = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color         = x.parent.color       # Випадок 2
                    x.parent.color  = BLACK
                    w.right.color   = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color         = BLACK
                    x.parent.color  = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color       = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color         = x.parent.color
                    x.parent.color  = BLACK
                    w.left.color    = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK
 
 
# ─── Головна програма ────────────────────────────────────────────────────────
 
if __name__ == "__main__":
    KEYS = [28, 76, 27, 10, 5, 35, 95, 16, 33]
 
    print("=" * 60)
    print(" ЧЕРВОНО-ЧОРНЕ ДЕРЕВО (RBT)")
    print(f" Послідовність: {KEYS}")
    print("=" * 60)
 
    t = RBTree()
    for k in KEYS:
        t.insert(k)
        print(f"  Вставлено {k}: inorder = {t.inorder()}")
 
    print(f"\n Висота RBT: {t.height()}")
    print(f" Чорна висота: {t.black_height()}")
    print(f"\n Inorder  (симетричний): {t.inorder()}")
    print(f" Preorder (прямий):      {t.preorder()}")
    print(f" Postorder(зворотний):   {t.postorder()}")
 
    print("\n Стек викликів симетричного обходу RBT:")
    t.inorder_stack_trace()
 
    print("\n" + "=" * 60)
    print(" ВИДАЛЕННЯ ЧОРНИХ ВУЗЛІВ З RBT")
    print("=" * 60)
 
    t2 = RBTree()
    for k in KEYS:
        t2.insert(k)
 
    print(f"\n  Початковий стан: {t2.inorder()}")
    print(f"  Корінь: {repr(t2.root)}")
 
    # Видаляємо чорні вузли
    black_nodes = [n for n in t2.inorder()
                   if t2._search(t2.root, n).color == BLACK]
    print(f"  Чорні вузли: {black_nodes}")
 
    for bk in black_nodes[:3]:
        print(f"\n  Видаляємо чорний вузол {bk}:")
        t2.delete(bk)
        print(f"  Результат: {t2.inorder()}")
