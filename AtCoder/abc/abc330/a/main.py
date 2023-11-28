from typing import List

N, L = map(int, input().split())
A: List[int] = list(map(int, input().split()))
ans: int = 0
for a in A:
    if a >= L:
        ans += 1
print(ans)
