N = int(input())
A = [[] for _ in range(N)]
for _ in range(N):
    a = input()
    A[_] = [ch for ch in a]
B = [["0" for _ in range(N)] for __ in range(N)]
for i in range(N):
    if i == 0:
        for j in range(N):
            if j+1 == N:
                B[i+1][j] = A[i][j]
            else:
                B[i][j+1] = A[i][j]
    elif i == N-1:
        for j in range(N):
            if j == 0:
                B[i-1][j] = A[i][j]
            else:
                B[i][j-1] = A[i][j]
    else:
        for j in range(N):
            if j == 0:
                B[i-1][j] = A[i][j]
            elif j == N-1:
                B[i+1][j] = A[i][j]
            else:
                B[i][j] = A[i][j]
for b in B:
    ans = ""
    for ch in b:
        ans += ch
    print(ans)
