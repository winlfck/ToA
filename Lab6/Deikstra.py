# Лабораторна робота №6
# Тема: Алгоритми на графах. Пошук найкоротшого шляху
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Алгоритм Дейкстри (Dijkstra's algorithm)
 
import heapq
 
INF = float('inf')
 
# ─── Граф варіант 8 (матриця суміжності, 0 = ребра немає) ───────────────────
G = [
    [0, 2, 5, 1, 0, 0, 7, 0],  # 1
    [2, 0, 0, 3, 6, 0, 0, 0],  # 2
    [5, 0, 0, 0, 2, 4, 4, 0],  # 3
    [1, 3, 0, 0, 5, 4, 9, 0],  # 4
    [0, 6, 2, 5, 0, 3, 0, 0],  # 5
    [0, 0, 4, 4, 3, 0, 0, 1],  # 6
    [7, 0, 4, 9, 0, 0, 0, 6],  # 7
    [0, 0, 0, 0, 0, 1, 6, 0],  # 8
]
N = len(G)
 
 
def dijkstra(graph, src=0):
    """
    Алгоритм Дейкстри — пошук найкоротших шляхів від вершини src до всіх інших.
    Використовує чергу з пріоритетом (min-heap).
    """
    dist    = [INF] * N
    prev    = [-1]  * N
    visited = [False] * N
    dist[src] = 0
 
    pq = [(0, src)]  # (відстань, вершина)
 
    print("=" * 60)
    print(f" АЛГОРИТМ ДЕЙКСТРИ  (стартова вершина: {src + 1})")
    print("=" * 60)
    fmt_dist = lambda d: ["∞" if x == INF else x for x in d]
    fmt_prev = lambda p: [x + 1 if x >= 0 else -1 for x in p]
    print(f"  Ініціалізація:")
    print(f"    dist = {fmt_dist(dist)}")
    print(f"    prev = {fmt_prev(prev)}")
    print(f"    pq   = {[(d, v+1) for d,v in pq]}\n")
 
    step = 1
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
 
        print(f"  Крок {step}: u={u+1}, dist[{u+1}]={d}")
        print(f"    Суміжні вершини: {[v+1 for v in range(N) if graph[u][v]>0]}")
 
        relaxed = False
        for v in range(N):
            w = graph[u][v]
            if w > 0 and not visited[v]:
                nd = dist[u] + w
                if nd < dist[v]:
                    print(f"    Релаксація: dist[{v+1}]={fmt_dist(dist)[v]} > "
                          f"dist[{u+1}]+w({u+1},{v+1}) = {dist[u]}+{w}={nd} → оновлюємо")
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
                    relaxed = True
 
        if not relaxed:
            print(f"    (оновлень немає)")
 
        print(f"    dist = {fmt_dist(dist)}")
        print(f"    prev = {fmt_prev(prev)}")
        print()
        step += 1
 
    return dist, prev
 
 
def reconstruct_path(prev, dst):
    """Відновлює шлях від стартової вершини до dst."""
    path = []
    v = dst
    while v != -1:
        path.append(v + 1)
        v = prev[v]
    return "→".join(map(str, reversed(path)))
 
 
if __name__ == "__main__":
    dist, prev = dijkstra(G, src=0)
 
    print("=" * 60)
    print(" РЕЗУЛЬТАТИ (найкоротші шляхи від вершини 1)")
    print("=" * 60)
    print(f"  {'Вершина':^8} {'Відстань':^10} {'Маршрут'}")
    print(f"  {'-'*8} {'-'*10} {'-'*25}")
    for v in range(N):
        d = dist[v] if dist[v] != INF else "∞"
        p = reconstruct_path(prev, v)
        print(f"  {v+1:^8} {str(d):^10} {p}")
