def rot(a):
    res = [""]*4
    for i in range(4):
        for j in range(4):
            res[j] = a[i][j]+res[j]
    return res

def draw(x, y, p, d, e):
    for i in range(4):
        for j in range(4):
            if p[i][j] == "#":
                nx, ny = i + x, j + y
                if nx<0 or nx>=4 or ny<0 or ny>=4 or e[nx][ny] == "#":
                    return False
                else:
                    d[nx][ny] = "#"
    return True

def able(e, p):
    for _ in range(4):
        for i in range(4):
            for j in range(4):
                d = [list(e[k]) for k in range(4)]
                if not draw(i, j, p, d, e):
                    continue
                if e == d:
                    return True
                p = rot(p)
    return False

p = [list(input().split()[0]) for _ in range(12)]
s = []
s.append(p[:4])
s.append(p[4:8])
s.append(p[8:12])
d = [list("."*4) for _ in range(4)]
for i in range(3):
    if not able(d, s[i]):
        print("No")
        break
else:
    print("Yes")
