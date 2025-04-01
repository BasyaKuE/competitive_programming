import bisect
import itertools
import sys
import collections

MOD = 998244353

def count_digits(x):
    return len(str(x))

def calculate_contributions(A):
    global MOD
    N = len(A)
    # 長さと累積度数のマップ
    pow10 = [1]
    max_len = 11  # 10^9の最大桁数は10桁、余裕をもって11
    for _ in range(1, max_len + 1):
        pow10.append((pow10[-1] * 10) % MOD)

    contrib_pref = [0] * N
    contrib_suff = [0] * N

    count_based_on_length = [0] * (max_len + 1)  # 数 i の対応する貢献をキャッシュするためのもの

    # 各要素についてその数が末尾に来る時と先頭に来る時の貢献を計算する.
    for i in range(N):
        Ai_len = count_digits(A[i])

        # A[i] is in suffix
        contrib_suff[i] = (A[i] % MOD * count_based_on_length[Ai_len]) % MOD

        # A[i] is in prefix (calculate real-time)
        Ai_pow10_length = pow10[Ai_len]
        temp_contrib = 0
        x = A[i]
        for j in range(1, max_len + 1):
            count_based_on_length[j] = (count_based_on_length[j] + Ai_pow10_length) % MOD
            temp_contrib = (temp_contrib + x * (pow10[j] - 1) % MOD) % MOD
        contrib_pref[i] = temp_contrib % MOD

    result = (sum(contrib_pref) + sum(contrib_suff)) % MOD
    return result

def main():

    N = int(input())
    A = list(map(int, input().split()))

    result = calculate_contributions(A)
    print(result)

main()
