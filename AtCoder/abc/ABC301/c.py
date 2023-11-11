# 解説AC
from collections import defaultdict, Counter
atcoder = [c for c in "atcoder"]
S = input()
T = input()
S_d, T_d = Counter(S), Counter(T)
S_at, T_at = S_d["@"], T_d["@"]
dif = abs(S_at-T_at)
for s in S_d:
    if s == "@":
        continue
    if s in atcoder:
        dif -= abs(S_d[s] - T_d)
print("Yes")
