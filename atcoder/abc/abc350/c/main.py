N = int(input())
A = list(map(int, input().split()))
pos = [0 for _ in range(N)]
for i in range(N):
    pos[A[i]-1] = i
ans = []
for i in range(N):
    if A[i] != i+1:
        ans.append([i+1, pos[i]+1])
        j = A[i] - 1
        A[i], A[pos[i]] = A[pos[i]], A[i]
        pos[i], pos[j] = pos[j], pos[i]
print(len(ans))
for a in ans:
    print(*a)
