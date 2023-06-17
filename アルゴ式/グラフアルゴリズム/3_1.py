N, M = map(int, input().split())
G = [[] for _ in range(N)]
chk = [False for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
for k in range(N):
    ans = []
    if k == 0:
        chk[k] = True
        ans.append(k)
    else:
        for i in range(len(next)):
            ch = G[next[i]]
            for j in range(len(ch)):
                if chk[ch[j]] == False:
                    chk[ch[j]] = True
                    ans.append(ch[j])
    next = ans
    print(*sorted(ans))
