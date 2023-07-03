N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    c = C[i]
    if c in D:
        ans += P[D.index(c)+1]
    else:
        ans += P[0]
print(ans)
