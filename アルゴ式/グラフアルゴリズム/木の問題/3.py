def dfs(G, ):
    chk = G[i]
    if len(chk) == 0:
        return 

N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    G[a-1].append(b)
