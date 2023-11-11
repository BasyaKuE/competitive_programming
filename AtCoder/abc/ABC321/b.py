N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 101
for i in range(100+1):
    L = A + [i]
    # print(*L)
    chk = sum(L) - max(L) - min(L)
    if chk >= X:
        ans = i
        break
if ans == 101:
    print(-1)
else:
    print(ans)
