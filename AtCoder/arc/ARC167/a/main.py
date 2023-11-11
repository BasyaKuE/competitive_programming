N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
D = [0 for _ in range(M)]
for i in range(N):
    if i < M:
        D[i] += A[i]
    else:
        break
# print(D)
for j in range(N-M):
    # print("D", D)
    D[-(1+j)] += A[i+j]
# print(D)
ans = 0
for d in D:
    ans += d*d
print(ans)
