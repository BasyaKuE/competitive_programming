from collections import defaultdict

S = input()
d = defaultdict(int)
for ch in S:
    d[ch] += 1
# print(d)
n = max(d.values())
chk = [0 for _ in range(n)]
for k, v in d.items():
    chk[v-1] += 1
for c in chk:
    if c == 0 or c == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")
