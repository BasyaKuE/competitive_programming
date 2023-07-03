N = 30
Pyramid = [list(map(int, input().split())) for _ in range(N)]

K = 0
ans = []
for i in range(N-1):
    py = Pyramid[i]
    for j in range(len(py)):
        if Pyramid[i+1][j] >= Pyramid[i+1][j]:
            if py[j] > Pyramid[i+1][j]:
                Pyramid[i+1][0] = py[0]
                K += 1
                ans.append([i, j, i+1, j])
        else:
            if py[j] > Pyramid[i+1][j+1]:
                Pyramid[i+1][0] = py[0]
                K += 1
                ans.append([i, j, i+1, j+1])

print(K)
for a in ans:
    print(*a)
#print(ans)
