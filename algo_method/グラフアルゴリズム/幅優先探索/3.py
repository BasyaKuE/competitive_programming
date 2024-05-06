H, W = map(int, input().split())
X0, Y0, X1, Y1 = map(int, input().split())
G = [input() for _ in range(H)]

visited = [[False for _ in range(W)] for _ in range(H)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, visited):
    stack = [(x, y)]
    ans = 0

    while stack:
        x, y = stack.pop()

        if x == X1 and y == Y1:
            return ans
        if visited[y][x]:
            continue

        visited[y][x] = True
        ans += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and G[ny][nx] != 'B' and not(visited[ny][nx]):
                stack.append((nx, ny))

    return ans


ans = dfs(X0, Y0, visited)
print(ans)
