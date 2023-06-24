# チュートリアル読んだ まだ解いてない！
import math
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(min(pow(2,K), N+1))
