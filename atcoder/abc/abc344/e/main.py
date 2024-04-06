import bisect
import itertools
import sys
from typing import List

def process_queries(N, A, queries):
    index_map = {val: idx for idx, val in enumerate(A)}
    A = A[:]

    for query in queries:
        if query[0] == 1:
            x, y = query[1], query[2]
            idx_x = index_map[x]
            index_map[y] = idx_x + 1
            A.insert(idx_x + 1, y)
            for i in range(idx_x + 2, len(A)):
                index_map[A[i]] = i
        elif query[0] == 2:
            x = query[1]
            idx_x = index_map[x]
            del A[idx_x]
            for i in range(idx_x, len(A)):
                index_map[A[i]] = i

    return A

N = int(input().strip())
A = list(map(int, input().strip().split()))
Q = int(input().strip())
queries = [list(map(int, input().strip().split())) for _ in range(Q)]
final_A = process_queries(N, A, queries)
print(' '.join(map(str, final_A)))
