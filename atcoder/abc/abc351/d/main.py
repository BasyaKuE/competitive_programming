H, W = map(int, input().split())
grid = [input() for _ in range(H)]

state = [[1 for _ in range(W)] for _ in range(H)]
# 0磁石, 1ok, 2隣接
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            state[i][j] = 0
        else:
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#':
                    grid[nx][ny] = 2

for s in state:
    print(s)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs_stack(x, y, visited):
    stack = [(x, y)]
    result = 1

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue

        visited[x][y] = True

        chk = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '#':
                chk = True
                break
        if chk:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.' and not visited[nx][ny]:
                result += 1
                stack.append((nx, ny))

    return result

max_freedom = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            visited = [[False] * W for _ in range(H)]
            max_freedom = max(max_freedom, dfs_stack(i, j, visited))
print(max_freedom)
