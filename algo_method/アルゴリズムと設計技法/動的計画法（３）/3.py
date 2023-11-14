N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[False for _ in range(M+1)] for _ in range(N+1)]
scores = [[0 for _ in range(M)] for _ in range(N+1)]
dp[0][0], scores[0][0] = True, B[0]
for i in range(N):
    for j in range(M):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+A[i-1] < M:
            dp[i+1][j+A[i-1]] = True
            scores[i+1][j+A[i-1]] = max(scores[i+1][j+A[i-1]], scores[i+1][j+A[i-1]]+B[i])
if dp[-1][-1]:
    print(scores[-1][-1])
else:
    print(-1)
