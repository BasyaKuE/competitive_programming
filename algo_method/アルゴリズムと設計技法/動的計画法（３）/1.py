N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1
for i in range(1, N):
    for j in range(M):
        if dp[i-1][j] != 0: # 真上のマスを見る
            dp[i][j] = 1
        #print(j, j-A[i-1])
        if j-A[i-1] >= 0 and dp[i-1][j-A[i-1]] != 0:
            dp[i][j] = 1
#print(dp)
print(dp[-1].count(1))

