from typing import List

N, L, R = map(int, input().split())
A: List[int] = list(map(int, input().split()))
ans: List[int] = []
for a in A:
    if L <= a <= R:
        x = a
    elif a < L:
        x = L
    else:
        x = R
    ans.append(x)
print(*ans)
