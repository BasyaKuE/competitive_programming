N, M = map(int, input().split())
G = [[] for _ in range(N)]
flag = [False for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
d = [0 for _ in range(N)]
for target in range(N):
    cnt = 0
    for i in range(N):
        cnt += 1
        g = G[i]
        if target in g:
            d[target] = cnt
            break
        else:
            for j in range(len(g)):
                next_g = G[g[j]]

