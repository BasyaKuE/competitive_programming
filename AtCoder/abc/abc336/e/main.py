import bisect
import itertools
import sys
from typing import List

def calc_dp():
    # dp[i][j][k] は、最上位からi桁目まで見たときに、
    # 桁和がj、n未満である保証がある場合はk=1、そうでない場合はk=0、を表す。
    # ここで dp の実装部分は省略されています
    pass

# 各桁でのDPテーブルを計算
dp = calc_dp()

def count_good_numbers(N):
    # N の文字列表現
    S = str(N)
    # 桁数
    D = len(S)
    # 最終的なカウントを保持する変数
    count = 0
    # ここまでの桁和
    sum_digits = 0

    # 最上位の桁から順に、桁DPを用いて数え上げる
    for i in range(D):
        digit = int(S[i])
        # 現在の桁より小さい数字について、それがNより小さくなることが保証される
        for j in range(digit):
            # 残りの桁が0から9の任意の値を取る場合で、
            # これまでの桁和（sum_digits + j）で N を割り切れるパターンの個数をカウント
            if (sum_digits + j) > 0:
                count += dp[i+1][sum_digits+j][N < (sum_digits+j)*(10**(D-i-1))]

        # N が現在の桁でNと同じになる境界を超えるかどうかをチェック
        sum_digits += digit
        if sum_digits == 0:
            break
    # 最後に、N自身が条件を満たすかどうかチェック
    if N % sum_digits == 0:
        count += 1

    return count

# 実際に問題を解くためのメインプログラム
def main():
    N = int(input())
    result = count_good_numbers(N)
    print(result)

if __name__ == '__main__':
    main()
