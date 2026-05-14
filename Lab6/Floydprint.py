# Лабораторна робота №6
# Тема: Алгоритми на графах. Пошук найкоротшого шляху
# Студент: Кириленко М.О., група АІ-245, варіант 8
# Алгоритм Флойда-Уоршелла (Floyd-Warshall algorithm)
 
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
 
 
def fmt(x):
    return "∞" if x == INF else str(x)
 
 
def print_matrix(D, label=""):
    if label:
        print(f"  {label}")
    header = "     " + "  ".join(f"{j+1:>3}" for j in range(N))
    print(header)
    print("  " + "-" * (N * 5 + 2))
    for i in range(N):
        row = "  ".join(f"{fmt(D[i][j]):>3}" for j in range(N))
        print(f"  {i+1} | {row}")
    print()
 
 
def floyd(G):
    """
    Алгоритм Флойда-Уоршелла.
    Обчислює матрицю найкоротших відстаней між усіма парами вершин.
    D[i][j] = мінімальна відстань від i до j.
    Рекурентне співвідношення: D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    """
    # Ініціалізація: D^(0) = вагова матриця
    D = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                D[i][j] = 0
            elif G[i][j] > 0:
                D[i][j] = G[i][j]
 
    print("=" * 60)
    print(" АЛГОРИТМ ФЛОЙДА-УОРШЕЛЛА")
    print("=" * 60)
    print_matrix(D, "D^(0) — початкова вагова матриця:")
 
    for k in range(N):
        updated = []
        for i in range(N):
            for j in range(N):
                if D[i][k] + D[k][j] < D[i][j]:
                    old = D[i][j]
                    D[i][j] = D[i][k] + D[k][j]
                    updated.append(
                        f"    d[{i+1}][{j+1}]: min({fmt(old)}, "
                        f"d[{i+1}][{k+1}]+d[{k+1}][{j+1}]) "
                        f"= min({fmt(old)}, {D[i][k]}+{D[k][j]}) = {D[i][j]}"
                    )
        print(f"  k={k+1} (проміжна вершина {k+1}):")
        if updated:
            for u in updated:
                print(u)
        else:
            print("    (змін немає)")
        print_matrix(D, f"D^({k+1}):")
 
    return D
 
 
if __name__ == "__main__":
    D = floyd(G)
 
    print("=" * 60)
    print(" ФІНАЛЬНА МАТРИЦЯ НАЙКОРОТШИХ ВІДСТАНЕЙ D^(8):")
    print("=" * 60)
    print_matrix(D)
 
    print("  Рядок 1 (від вершини 1 до всіх):")
    for j in range(N):
        print(f"    1→{j+1}: {fmt(D[0][j])}")
