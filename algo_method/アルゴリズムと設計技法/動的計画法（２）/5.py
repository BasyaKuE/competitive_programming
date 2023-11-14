N = int(input())
G = [input() for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if (i == 0 and j == 0) or G[i][j] == "#":
            continue
        elif i == 0 or G[i-1][j] == "#":
            dp[i][j] = dp[i][j-1]
        elif j == 0 or G[i][j-1] == "#":
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1])
