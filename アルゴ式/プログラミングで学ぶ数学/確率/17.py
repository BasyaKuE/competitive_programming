import math
N, M = map(int, input().split())
if (N+M) % 2 == 0:
    p = (N+M)//2
    # print("p", p)
    ans = math.comb(N, p)/(2**N)
    print(ans)
else:
    print(0)
