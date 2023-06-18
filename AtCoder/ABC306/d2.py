N = int(input())
dp = [[0,0] for _ in range(N)]
for i in range(N):
    X, Y = map(int, input().split())
    if i == 0:
        if X == 0:
            dp[0][0] = max(Y, 0)
            dp[0][1] = 0
        else:
            dp[0][0] = 0
            dp[0][1] = Y
    else:
        if X == 0:
            dp[i][0] = max([dp[i-1][0], dp[i-1][0]+Y, dp[i-1][1]+Y])
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][0]+Y, dp[i-1][1])
print(max(dp[-1]))
