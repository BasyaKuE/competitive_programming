Ha, Wa = map(int, input().split())
A = [input() for _ in range(Ha)]

Hb, Wb = map(int, input().split())
B = [input() for _ in range(Hb)]

preHx, preWx = map(int, input().split())
preX = [input() for _ in range(preHx)]

rec = []
f = False
for i in range(preHx):
    for j in range(preWx):
        if preX[i][j] == "#":
            rec.append((i, j))
print(rec)

for r in rec:
    ch

Hc, Wc = 30, 30
C = ["."*30 for _ in range(30)]

