def rec(G, v, target):
    

N = int(input())
P = list(map(int, input().split()))
now = 0
ans = [0 for _ in range(N)]
chk = [False for _ in range(N)]
chk[0] = True
cnt = 0
while chk.count(False) != 0:
    for i in range(N-1):
        if P[i] == now:
            now = i
            break
    cnt += 1
    chk[now] == True
    ans[now] = cnt
