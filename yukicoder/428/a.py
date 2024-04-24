N, K = map(int, input().split())
before = [input() for _ in range(N)]

ans = []
for i in range(N):
    row = ""
    for j in range(N):
        row += before[i][j]
        for k in range(K-1):
            row += before[i][j]
    ans.append(row)
    for _ in range(K-1):
        ans.append(row)
for row in ans:
    print(row)
