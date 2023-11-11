N, M, P = map(int, input().split())
cnt = 0
for i in range(N):
    if i+1 == M:
        cnt += 1
    elif (i+1-M) % P == 0:
        cnt += 1
print(cnt)
