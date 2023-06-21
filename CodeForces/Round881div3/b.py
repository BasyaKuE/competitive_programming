# チュートリアルAC

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans1, ans2 = 0, 0
    flag = False
    for i in range(N):
        if flag == False and A[i] < 0:
            ans2 += 1
            flag = True
        if flag and A[i] > 0:
            flag = False
        ans1 += abs(A[i])
    print(ans1, ans2)
