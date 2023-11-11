N, M = map(int, input().split())
paths = [[-1 for _ in range(N)] for __ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    paths[A-1][B-1] = C
    paths[B-1][A-1] = C


def dfs(start, paths, N):
    max_dis = 0
    stack = [(start, 0, [False]*N)]
    while stack:
        now, s, visited = stack.pop()
        visited[now] = True
        max_dis = max(max_dis, s)

        for i in range(N):
            if not visited[i] and paths[now][i] != -1:
                stack.append((i, s+paths[now][i], visited.copy()))
    return max_dis


ans = 0
for i in range(N):
    ans = max(ans, dfs(i, paths, N))
print(ans)
