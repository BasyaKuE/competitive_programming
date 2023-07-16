# import random
# N = 10**4
# S = "".join(str(random.randint(0, 1)) for _ in range(N))

N = int(input())
S = input().strip()
A = [int(c) for c in S]
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = A[i]

for l in range(2, N+1):
    for i in range(N - l + 1):
        j = i + l - 1
        dp[i][j] = int(
            (dp[i][j-1] == 0 or A[j] == 0) and
            not (dp[i][j-1] == 1 and A[j] == 1)
            )
# print(dp)
ans = sum(sum(row) for row in dp)
print(ans)
