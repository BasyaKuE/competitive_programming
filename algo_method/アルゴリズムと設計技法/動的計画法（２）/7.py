N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N-1, -1, -1):
        if i == 0 and j == N-1:
            dp[i][j] = A[i][j]
        elif i == 0:
            dp[i][j] = A[i][j] + dp[i][j+1]
        elif j == N-1:
            dp[i][j] = A[i][j] + dp[i-1][j]
        else:
            dp[i][j] = A[i][j] + min(dp[i][j+1], dp[i-1][j])
print(dp[-1][0])
