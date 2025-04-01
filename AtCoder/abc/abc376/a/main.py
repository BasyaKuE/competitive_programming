N, C = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
now = 0
for i in range(N):
    if i == 0:
        ans += 1
        now = T[i]
    elif T[i] - now >= C:
        ans += 1
        now = T[i]
    else:
        # print("fail", T[i])
        pass
print(ans)
