N = int(input())
S = [input() for _ in range(N)]

hash_set = set()

for s in S:
    str1 = ''.join(sorted([s, s[::-1]]))
    hash_set.add(str1)

print(len(hash_set))
