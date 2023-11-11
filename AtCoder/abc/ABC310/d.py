import itertools
N, T, M = map(int, input().split())
bad_pair = [list(map(int, input().split())) for _ in range(M)]
ans = 0
conb = itertools.combinations(list(range(N)))
