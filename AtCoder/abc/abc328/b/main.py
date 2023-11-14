from typing import List, Set

N: int = int(input())
D: List[int] = list(map(int, input().split()))
ans: int = 0
for i in range(N):
    if len(set(str(i+1))) != 1:
        continue
    for j in range(D[i]):
        chk: Set[str] = set(list(str(j+1)))
        # print("c", chk, list(chk)[0])
        if len(chk) == 1 and list(chk)[0] == list(str(i+1))[0]:
            ans += 1
print(ans)
