N, M = map(int, input().split())
A = list(map(int, input().split()))
day = 1
for i in range(M):
    a = A[i]
    for j in range(a-day+1):
        print(a-day)
        day += 1
