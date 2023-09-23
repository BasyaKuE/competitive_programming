S = input()
N = len(S)
ans = -1
for i in range(N):
    for j in range(i+1, N+1):
        chk = S[i:j]
        # print(chk, chk[::-1])
        if chk == chk[::-1] and len(chk) > ans:
            ans = len(chk)
print(ans)
