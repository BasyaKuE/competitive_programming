N, M = map(int, input().split())
rec = [True for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    rec[B-1] = False
if rec.count(True) >= 2 or rec.count(True) == 0:
    print(-1)
    exit()
for i in range(N):
    if rec[i]:
        print(i+1)
        break
