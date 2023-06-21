N, M = map(int, input().split())
W = list(map(int, input().split()))
dp = [[False for _ in range(M+1)] for _ in range(N+1)] # 0番目は入れないって何も入れないって意味
dp[0][0] = True
for i in range(1,N):
    for j in range(M):
        if dp[i-1][j]:
            dp[i][j] = True
        if j-W[i-1] >= 0 and dp[i-1][j-W[i-1]]:
            dp[i][j] = True
print(dp)
if dp[-1][-1]:
    print("Yes")
else:
    print("No")
