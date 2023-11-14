N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(1,N):
    if i == 1:
        dp[i] = A[i]
    else:
        dp[i] = min(dp[i-1]+A[i], dp[i-2]+2*A[i])
print(dp[-1])
