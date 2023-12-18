import bisect
import itertools
import sys
from typing import List

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

bad_combinations = set()
for _ in range(L):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    bad_combinations.add((c, d))

max_price = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in bad_combinations:
            price = A[i] + B[j]
            max_price = max(max_price, price)
print(max_price)
