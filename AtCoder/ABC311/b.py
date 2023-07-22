N, D = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
chk = 0
for i in range(D):
    flag = True
    for j in range(N):
        if S[j][i] == "x":
            flag = False
    if flag:
        chk += 1
    else:
        ans = max(ans, chk)
        chk = 0
ans = max(ans, chk)
print(ans)
