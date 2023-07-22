H, W, N = map(int, input().split())
holes = [list(map(int, input().split())) for _ in range(N)]

grid = [[1]*W for _ in range(H)]
for a, b in holes:
    grid[a-1][b-1] = 0

dp = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == 1:
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 1

answer = sum(sum(row) for row in dp)
print(answer)
