import sys
from collections import deque, defaultdict

def bfs(u, g):
    dist = [-1] * (N1 + N2 + 2)
    dist[u] = 0
    queue = deque([u])
    while queue:
        v = queue.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    return dist

def solve():
    sys.setrecursionlimit(10**6)

    # グラフの初期化
    g = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)

    # 最初の部分の最遠ノードを見つける
    dist1 = bfs(1, g)
    max_node1 = dist1.index(max(dist1[1:N1+1]))

    # 二つ目の部分の最遠ノードを見つける
    dist2 = bfs(N1+1, g)
    max_node2 = dist2.index(max(dist2[N1+1:N1+N2+1])) + N1

    # 最大距離を求める
    max_dist = max(dist1) + max(dist2) + 1

    print(max_dist)


if __name__ == '__main__':
    N1, N2, M = map(int, sys.stdin.readline().split())
    solve()
