import itertools

M = int(input().strip())
R1 = input()
R2 = input()
R3 = input()

chk = [[[], [], []] for _ in range(10)]

for i in range(10):
    for j in range(M):
        # R1
        if R1[j] == str(i):
            chk[i][0].append(j)

        # R2
        if R2[j] == str(i):
            chk[i][1].append(j)

        # R3
        if R3[j] == str(i):
            chk[i][2].append(j)
# print(chk)
flag = True
for i in chk:
    if i[0] and i[1] and i[2]:
        flag = False
        break
if flag:
    print(-1)
    exit()
ans = float("inf")
for i in range(10):
    l = chk[i]
    for comb in itertools.product(*l):
        # print(comb)
        if len(comb) != len(set(comb)):
            ans = min(ans, max(comb)+M)
        else:
            ans = min(ans, max(comb))
print(ans)
