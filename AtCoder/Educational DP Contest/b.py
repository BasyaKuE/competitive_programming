import math
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [math.inf for _ in range(N)]
dp[0] = h[1]
for i in range(1, N):
    if i == 1:
        dp[i] = abs(h[i]-h[i-1])
    elif i <= K:
        dp[i] = min([])
