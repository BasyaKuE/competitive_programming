N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

nodes = [0]

dist = [-1]*N

nodes = [[] for _ in range(N)]

dist[0] = 0
nodes[0] = [0]

for k in range(1, N):
    for v in nodes[k-1]:
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue

            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)
print(max(dist))
