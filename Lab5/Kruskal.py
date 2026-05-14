# Лабораторна робота №5
# Тема: Алгоритми на графах. Мінімальне кістякове дерево
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Алгоритм Крускала (Kruskal's algorithm)
 
# ─── Граф варіант 8 ──────────────────────────────────────────────────────────
EDGES = [
    (1,2,2),(1,3,5),(1,4,1),(1,7,7),
    (2,4,3),(2,5,6),
    (3,5,2),(3,6,4),(3,7,4),
    (4,5,5),(4,6,4),(4,7,9),
    (5,6,3),
    (6,8,1),
    (7,8,6)
]
 
# ─── Структура DSU (Disjoint Set Union / Union-Find) ─────────────────────────
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank   = [0] * (n+1)
 
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # стиснення шляху
            x = self.parent[x]
        return x
 
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False   # цикл
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True
 
 
def kruskal(edges, n=8):
    """Алгоритм Крускала — додаємо ребра у порядку зростання ваги, уникаючи циклів."""
    sorted_edges = sorted(edges, key=lambda e: e[2])
    dsu = DSU(n)
    mst = []
    total = 0
 
    print("=" * 60)
    print(" АЛГОРИТМ КРУСКАЛА — Мінімальне кістякове дерево")
    print("=" * 60)
    print(f" Відсортовані ребра:")
    for u,v,w in sorted_edges:
        print(f"   {u}-{v} : {w}")
    print()
 
    step = 1
    for u,v,w in sorted_edges:
        if dsu.union(u,v):
            mst.append((u,v,w))
            total += w
            print(f"  Крок {step}: Додаємо {u}-{v} (вага={w})")
            print(f"    ET = {{{', '.join(f'{a}-{b}={c}' for a,b,c in mst)}}}\n")
            step += 1
            if len(mst) == n - 1:
                break
        else:
            print(f"  Пропускаємо {u}-{v} (вага={w}) — утворює цикл")
 
    print("-" * 60)
    print(" МКД (Крускала):")
    for u,v,w in mst:
        print(f"   {u}-{v} : {w}")
    print(f"\n Сумарна вага: {total}")
    return mst, total
 
if __name__ == "__main__":
    kruskal(EDGES)
