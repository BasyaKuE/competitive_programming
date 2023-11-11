N = int(input())
abcd = []
total = 0
max_b, max_d = 0, 0
for i in range(N):
    a, b, c, d = map(int, input().split())
    max_b = max(max_b, b)
    max_d = max(max_d, d)
    abcd.append([a, b, c, d])
cell = [[0 for _ in range(max_b)] for _ in range(max_d)]
for i in range(N):
    a, b, c, d = abcd[i][0], abcd[i][1], abcd[i][2], abcd[i][3]
    for j in range(c-1, d-1):
        for k in range(a-1, b-1):
            cell[j][k] = 1
ans = 0
for i in range(max_d):
    for j in range(max_b):
        if cell[i][j] == 1:
            ans += 1
print(ans)
