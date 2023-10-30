N, K, P = map(int,input().split())
plans = [list(map(int,input().split())) for _ in range(N)]
INF = 1<<60

dp1 = [INF]*((1<<K)+1)
dp1[0] = 0
idxs = list(range(K))
idxs.sort(key = lambda i : -plans[0][i+1])

for i in range(1<<K):
    if dp1[i]==INF: continue

    cost_benefit = []
    for j, idx in enumerate(idxs):
        dp2 = dp1[:]
        add = 1<<idx
        cost, a = plans[0][0], plans[0][idx+1]
        for k in range(P):
            if k>=a: break
            if i&add:
                dp2[i] = min(dp2[i], dp1[i^add] + cost)
            else:
                dp2[i|add] = min(dp2[i|add], dp1[i] + cost)
            cost_benefit.append((dp2[i|add]-dp2[i], (idx, cost)))
            cost *= 2
        dp1 = dp2[:]
    cost_benefit.sort(reverse=True)

    while cost_benefit:
        _, (idx, cost) = cost_benefit.pop()
        dp2 = dp1[:]
        add = 1<<idx
        for k in range(P):
            if dp1[i|add] + cost >= dp2[i|add]: break
            dp2[i|add] = min(dp2[i|add], dp1[i] + cost)
            cost *= 2
        dp1 = dp2[:]

print(dp1)
if dp1[-1]==INF:
    print(-1)
else:
    print(dp1[-1])
