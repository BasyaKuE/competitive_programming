from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N+1)]
for u, v, x, y in edges:
    G[u].append((v, x, y))
    G[v].append((u, -x, -y))

INF = float('inf')
pos = [(INF, INF) for _ in range(N+1)]
pos[1] = (0, 0)

for s in range(1, N+1):
    if pos[s] == (INF, INF):
        continue

    q = deque([(s, *pos[s])])
    while q:
        v, x, y = q.popleft()
        for nv, dx, dy in G[v]:
            if pos[nv] == (INF, INF):
                pos[nv] = (x + dx, y + dy)
                q.append((nv, x + dx, y + dy))
            elif pos[nv] != (x + dx, y + dy):
                print('undecidable')
                break
for x, y in pos[1:]:
    if x == float("inf") and y == float("inf"):
        print("undecidable")
    else:
        print(x, y)
