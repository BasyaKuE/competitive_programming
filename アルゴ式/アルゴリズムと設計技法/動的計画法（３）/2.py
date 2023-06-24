N, M = map(int, input().split())
W = list(map(int, input().split()))
dp = [[False for _ in range(M+1)] for _ in range(N+1)] # 0番目は入れないって何も入れないって意味
dp[0][0] = True
for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j]: # 重さを加えない
            dp[i][j] = True
        if dp[i-1][j] and j+W[i-1] < M+1: # 重さを加える（くわえられるなら）
            dp[i][j+W[i-1]] = True
if dp[-1][-1]:
    print("Yes")
else:
    print("No")
