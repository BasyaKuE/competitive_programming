N, M = map(int, input().split())
INFO = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if INFO[i][0] >= INFO[j][0]:
            F_i = INFO[i][2:]
            F_j = INFO[j][2:]
            flag = True
            for f in F_i:
                if f in F_j:
                    continue
                else:
                    flag = False
                    break
            if flag and (INFO[i][0] > INFO[j][0] or len(F_j) > len(F_i)):
                print("Yes")
                exit()
print("No")
