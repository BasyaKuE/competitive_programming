from typing import List

N, Q = map(int, input().split())
S: str = input()

# 累積和
cumulative: List[int] = [0] * N
for i in range(1, N):
    cumulative[i] = cumulative[i - 1]
    if S[i] == S[i - 1]:
        cumulative[i] += 1

for _ in range(Q):
    l, r = map(int, input().split())
    ans: int = cumulative[r - 1] - cumulative[l - 1]
    print(ans)
