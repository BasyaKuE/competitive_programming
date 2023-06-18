A1, A2, A3, A4 = map(int, input().split())
dp = [[0, 0, 0, 0] for _ in range(4)]
dp[0] = [A1, A2, A3, A4]
for i in range(1, 4):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
    dp[i][2] = dp[i-1][1]+dp[i-1][2]+dp[i-1][3]
    dp[i][3] = dp[i-1][2]+dp[i-1][3]
print(dp[-1][-1])
