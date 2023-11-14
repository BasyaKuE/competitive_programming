N, M = map(int, input().split())
D = list(map(int, input().split()))
dp = [False for _ in range(N+1)]
dp[0] = True
for i in range(1, N+1):
    for j in range(M):
        d = D[j]
        if i-d >= 0 and dp[i-d] == True:
            dp[i] = True
            break
if dp[-1]:
    print("Yes")
else:
    print("No")
