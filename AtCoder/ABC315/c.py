N = int(input())
f_set = set()
f_max = [-1 for _ in range(N+1)]
ice = dict()
for _ in range(N):
    F, S = map(int, input().split())
    f_set.add(F)
    if F in ice:
        ice[F].append(S)
    else:
        ice[F] = [S]
    f_max[F] = max(f_max[F], S)
f_max.sort(reverse=True)
ans = f_max[0] + f_max[1]
for i in f_set:
    ice[i].sort(reverse=True)
for k, v in ice.items():
    if len(v) == 1:
        continue
    ans = max(ans, v[0] + v[1]//2)
print(ans)
