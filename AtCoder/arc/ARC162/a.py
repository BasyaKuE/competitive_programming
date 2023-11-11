T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    chk = [True for _ in range(N)]
    for i in range(1, N):
        chk = P[0:i-1]

        if max(chk) < P[i]:
            ans += 1
    print(ans)


"""
20
13 2 7 1 5 9 3 4 12 10 15 6  8  14 20 16 19 18 11 17
1  2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 18 19 20

今trueは13, 15, 20

可能性があるのは13, 14, 20, 16, 19,

ありそうなのは18

自分より前にいるやつが往路でも前にいればおけ

5
1 2 3 5 4
-> 4

5
2 1 3 4 5
-> 4
"""
