from typing import List

N, M = map(int, input().split())
S: List[str] = [input() for _ in range(N)]
for i in range(N-8):
    for j in range(M-8):
        chk: List[str] = [S[i+k][j:j+9] for k in range(9)]
        black_flag: bool = True
        white_flag: bool = True
        for k in range(3):
            for l in range(3):
                if chk[k][l] == "#" and chk[k+6][l+6] == "#":
                    continue
                else:
                    black_flag = False
                    break
        for k in range(3):
            if chk[k][3] == "." and chk[k+6][5] == ".":
                continue
            else:
                white_flag = False
        if chk[3][0:4] == "...." and chk[5][5:] == "....":
            pass
        else:
            white_flag = False
        if black_flag and white_flag:
            print(i+1, j+1)

