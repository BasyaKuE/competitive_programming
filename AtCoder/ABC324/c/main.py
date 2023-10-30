from typing import List

N_str, T_dash = map(str, input().split())
N: int = int(N_str)
ans: List[int] = []
for i in range(N):
    S: str = input()
    head_cnt: int = 0
    if T_dash == S:
        ans.append(i+1)
        continue
    if abs(len(T_dash) - len(S)) > 1:
        continue
    L: int = min(len(T_dash), len(S))
    for j in range(L):
        if T_dash[j] != S[j]:
            break
        head_cnt += 1
    tail_cnt: int = 0
    for j in range(L):
        if T_dash[-(j+1)] != S[-(j+1)]:
            break
        tail_cnt += 1
    chk: int = head_cnt + tail_cnt
    if chk >= len(S) and len(S) == len(T_dash)-1:
        # print("ok!", i+1)
        ans.append(i+1)
    elif chk >= len(S) - 1 and len(S) - 1 == len(T_dash):
        ans.append(i+1)
    elif chk == len(S) - 1 and len(S) - 1 == len(T_dash) - 1:
        ans.append(i+1)
    # print(i+1, S, head_cnt, tail_cnt, chk)
print(len(ans))
print(*ans)
