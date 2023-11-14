from typing import List

N, X = map(int, input().split())
S: List[int] = list(map(int, input().split()))
ans: int = 0
for i in range(N):
    if S[i] <= X:
        ans += S[i]
print(ans)
