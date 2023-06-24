N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(N):
    if i < K:
        for j in range(i):
            dp[i] = min(dp[i], dp[i-j]+abs(H[i]-H[j]))
    else:
        for j in range(K):
            dp[i] = min(dp[i], dp[i-j]+abs(H[i]-H[j]))
print(dp)
print(dp[-1])
