import bisect
import itertools
import sys
from typing import List

# 6, 8, 12
N, S, M, L = map(int, input().split())
P = {"6": S, "8": M, "12": L}

best_cost = float('inf')

for s_pack in range((N + 5) // 6 + 1):
    for m_pack in range((N + 7) // 8 + 1):
        l_pack = (N - (s_pack * 6 + m_pack * 8) + 11) // 12
        if l_pack < 0:
            continue
        if s_pack * 6 + m_pack * 8 + l_pack * 12 >= N:
            cost = s_pack * S + m_pack * M + l_pack * L
            best_cost = min(best_cost, cost)

print(best_cost)
