N = int(input())
G = [[0 for _ in range(N)] for _ in range(N)]
G[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            G[i][j] = G[i][j-1]
        elif j == 0:
            G[i][j] = G[i-1][j]
        else:
            G[i][j] = G[i][j-1] + G[i-1][j]
#print(G)
print(G[-1][-1])
