import sys

sys.setrecursionlimit(5000)

H, W = map(int, input().split())
X0, Y0, X1, Y1 = map(int, input().split())
G = [input() for _ in range(H)]

nodes = [[X0, Y0]]
dist = [[-1 for _ in range(W)] for __ in range(H)]
chk = [[float('inf') for _ in range(W)] for __ in range(H)]

nodes = [[] for _ in range(H*W)]

dist[X0][Y0] = 0
nodes[0] = [X0, Y0]

cnt = 0
print(dist)


def dfs(x, y, G, dist, cnt):
    cnt += 1
    chk[x][y] = min(cnt, dist[x][y])
    dist[x][y] = 0
    if x-1 >= 0 and G[x-1][y] == "W" and dist[x-1][y] == -1:
        dfs(x-1, y, G, dist, cnt)
    if y-1 >= 0 and G[x][y-1] == "W" and dist[x][y-1] == -1:
        dfs(x, y-1, G, dist, cnt)
    if x+1 < W and G[x+1][y] == "W" and dist[x+1][y] == -1:
        dfs(x+1, y, G, dist, cnt)
    if y+1 < H and G[x][y+1] == "W" and dist[x][y+1] == -1:
        dfs(x, y+1, G, dist, cnt)


dfs(X0, Y0, G, dist, cnt)
print(dist[X1][Y1])
