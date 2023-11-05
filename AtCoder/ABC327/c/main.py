from typing import List, Set

A: List[List[int]] = [list(map(int, input().split())) for _ in range(9)]

# 行
for i in range(9):
    row = A[i]
    chk: Set = set()
    for j in range(9):
        chk.add(row[j])
    if len(chk) != 9:
        print("No")
        exit()

# 列
for j in range(9):
    chk = set()
    for i in range(9):
        row = A[i]
        chk.add(row[j])
    if len(chk) != 9:
        print("No")
        exit()

# それぞれ3*3
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        # ここから良い感じにして
        chk = set()
        for x in range(3):
            for y in range(3):
                chk.add(A[i+x][j+y])
        if len(chk) != 9:
            print("No")
            exit()
print("Yes")
