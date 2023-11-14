N = int(input())
dp = [0 for _ in range(N)]
for i in range(N):
    if i == 0: #1段目
        dp[i] = 1
    elif i == 1: #2段め
        dp[i] = 2
    else:
        dp[i] = dp[i-1]+dp[i-2]
print(dp[-1])
