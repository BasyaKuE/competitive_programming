import sys

sys.setrecursionlimit(10**6)


def dfs(grid, N, M, i, j, visited):
    if grid[i][j] == '#' or (i == N-1 and j == M-1):
        return 0
    visited[i][j] = True
    return (1 + dfs(grid, N, M, i+1, j, visited) +
            dfs(grid, N, M, i-1, j, visited) +
            dfs(grid, N, M, i, j+1, visited) +
            dfs(grid, N, M, i, j-1, visited))


N, M = map(int, input().split())
G = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
ans = dfs(G, N, M, 1, 1, visited)
rock_cnt = 0
for i in range(N):
    rock_cnt += G[i].count("#")
print(ans)
