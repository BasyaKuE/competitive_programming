N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 最初の頂点集合 (スタートは頂点 0 のみ)
nodes = [0]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes = [[] for i in range(N)]

# 頂点 0 を始点とする
dist[0] = 0
nodes[0] = [0]

print(0)
# k 手目の探索をする
for k in range(1, N):
    ans = []
    # k-1 手目に探索された各頂点 v に対して
    for v in nodes[k - 1]:
        # 頂点 v から 1 手で行ける頂点 next_v を探索
        for next_v in G[v]:
            # 頂点 next_v が探索済みであれば何もしない
            if dist[next_v] != -1:
                continue

            # 頂点 next_v を探索する
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)
            ans.append(next_v)
    ans.sort()
    print(*ans)
