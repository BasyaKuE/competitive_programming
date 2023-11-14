N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
for i in range(3):
    dp[0][i] = A[0][i]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])+A[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2])+A[i][1]
    dp[i][2] = max(dp[i-1][1], dp[i-1][0])+A[i][2]
print(max(dp[-1]))
