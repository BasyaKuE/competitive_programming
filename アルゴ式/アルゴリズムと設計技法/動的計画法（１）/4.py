N = int(input())
dp = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 2
    elif i == 2:
        dp[i] = 4
    else:
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
#print(dp)
print(dp[-1])
