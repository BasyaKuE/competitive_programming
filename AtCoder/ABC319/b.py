from typing import List

N: int = int(input())
result: List[str] = []
for i in range(N+1):
    for j in range(1, 10):
        if N % j == 0 and i % (N//j) == 0:
            result.append(str(j))
            break
    else:
        result.append('-')
ans: str = ''.join(result)
print(ans)
