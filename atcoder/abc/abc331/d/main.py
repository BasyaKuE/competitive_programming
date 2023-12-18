import bisect
import itertools
import sys
from typing import List

# 標準入力からN, Q, およびパターンPを取得する
N, Q = map(int, input().split())
pattern = [input() for _ in range(N)]

# 各行と各列の黒マスの数を計算する
row_counts = [row.count('B') for row in pattern]
col_counts = [col.count('B') for col in zip(*pattern)]

# クエリを処理する関数
def count_black_cells(A, B, C, D):
    # 黒マスのトータル数を加算するための変数
    total_black_cells = 0

    # 縦のブロックの数とマスの数を計算
    height_blocks, height_rem = divmod(C - A + 1, N)
    width_blocks, width_rem = divmod(D - B + 1, N)

    # 縦に全てのブロックを通過する場合の黒マスの数を加算
    total_black_cells += sum(row_counts) * height_blocks * width_blocks * N

    # 残りの行と列に対して黒マスを加算
    for i in range(height_rem):
        total_black_cells += row_counts[(A + i) % N] * width_blocks * N
    for j in range(width_rem):
        total_black_cells += col_counts[(B + j) % N] * height_blocks * N

    # 交差部分の黒マスの数を加算
    for i in range(height_rem):
        for j in range(width_rem):
            if pattern[(A + i) % N][(B + j) % N] == 'B':
                total_black_cells += 1

    return total_black_cells

# クエリを読み込み、答えを出力
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(count_black_cells(A, B, C, D))
