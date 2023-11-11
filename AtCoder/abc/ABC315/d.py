H, W = map(int, input().split())
C = [list(input().strip()) for _ in range(H)]
while True:
    marked = set()
    for i in range(H):
        if len(set(C[i])) == 1 and C[i][0] != '.':
            for j in range(W):
                marked.add((i, j))
    for j in range(W):
        r = [C[i][j] for i in range(H) if C[i][j] != '.']
        if len(set(r)) == 1 and len(r) >= 2:
            for i in range(H):
                if C[i][j] != '.':
                    marked.add((i, j))
    if marked:
        for i, j in marked:
            C[i][j] = '.'
    else:
        break
cnt = 0
for i in range(H):
    for j in range(W):
        if C[i][j] != ".":
            cnt += 1
print(cnt)
