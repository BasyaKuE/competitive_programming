N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(1,N):
    if i == 1:
        dp[i] = A[i]
    else:
        chk = 10**18
        for j in range(1, M+1):
            chk = min(chk, dp[i-j]+j*A[i])
        dp[i] = chk
print(dp[-1])
