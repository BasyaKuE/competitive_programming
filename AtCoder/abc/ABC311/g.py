def solve(N, M, S):
    MOD = 998244353
    dp = [[[0]*(N+1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            for k in range(i+1):
                if j < M:
                    dp[i][j+1][max(k, S[i].count('#'))] += dp[i][j][k]
                    dp[i][j+1][max(k, S[i].count('#'))] %= MOD
                if i < N:
                    dp[i+1][j][k] += dp[i][j][k]
                    dp[i+1][j][k] %= MOD
    return sum(dp[N][M]) % MOD


N, M = map(int, input().split())
S = [input() for _ in range(N)]

print(solve(N, M, S))
