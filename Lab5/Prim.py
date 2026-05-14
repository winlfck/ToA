# Лабораторна робота №5
# Тема: Алгоритми на графах. Мінімальне кістякове дерево
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Алгоритм Прима (Prim's algorithm)
 
import heapq
 
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
 
def build_graph(edges, n=8):
    graph = {i: [] for i in range(1, n+1)}
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph
 
def prim(graph, start=1):
    """Алгоритм Прима — жадібне нарощування МКД від стартової вершини."""
    n = len(graph)
    visited = {start}
    mst_edges = []
    total = 0
 
    heap = [(w, start, v) for v,w in graph[start]]
    heapq.heapify(heap)
 
    print("=" * 60)
    print(" АЛГОРИТМ ПРИМА — Мінімальне кістякове дерево")
    print(f" Стартова вершина: {start}")
    print("=" * 60)
    print(f"  VT = {{{start}}}, ET = {{}}\n")
 
    step = 1
    while heap and len(visited) < n:
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u,v,w))
        total += w
        print(f"  Крок {step}: ребро {u}-{v} (вага={w})")
        print(f"    VT = {{{', '.join(map(str, sorted(visited)))}}}")
        print(f"    ET = {{{', '.join(f'{a}-{b}={c}' for a,b,c in mst_edges)}}}\n")
        for nb,nw in graph[v]:
            if nb not in visited:
                heapq.heappush(heap,(nw,v,nb))
        step += 1
 
    print("-" * 60)
    print(" МКД (Прима):")
    for u,v,w in mst_edges:
        print(f"   {u}-{v} : {w}")
    print(f"\n Сумарна вага: {total}")
    return mst_edges, total
 
if __name__ == "__main__":
    graph = build_graph(EDGES)
    prim(graph, start=1)
