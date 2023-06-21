T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    if N == 1:
        print(0)
    else:
        ans = 0
        for i in range(N//2):
            ans += A[-(1+i)]-A[i]
        print(ans)
