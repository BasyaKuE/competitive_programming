N, H, X = map(int, input().split())
P = list(map(int, input().split()))
chk = float("inf")
for i in range(N):
    if H+P[i] >= X and P[i] < chk:
        # print(P[i])
        ans = i+1
        chk = P[i]
print(ans)
