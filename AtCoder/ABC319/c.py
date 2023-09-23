from itertools import permutations

# がっかりするかどうかのチェック関数
def is_disappointed(order, c):
    for i in range(3):
        if c[i][0] == c[i][1] and c[i][0] != c[i][2] and order.index((i, 2)) > max(order.index((i, 0)), order.index((i, 1))):
            return True
        if c[0][i] == c[1][i] and c[0][i] != c[2][i] and order.index((2, i)) > max(order.index((0, i)), order.index((1, i))):
            return True
    if c[0][0] == c[1][1] and c[0][0] != c[2][2] and order.index((2, 2)) > max(order.index((0, 0)), order.index((1, 1))):
        return True
    if c[0][2] == c[1][1] and c[0][2] != c[2][0] and order.index((2, 0)) > max(order.index((0, 2)), order.index((1, 1))):
        return True
    return False

# 入力
c = [list(map(int, input().split())) for _ in range(3)]

total = 0
disappointed_count = 0

# すべての順列を生成
for order in permutations([(i, j) for i in range(3) for j in range(3)]):
    total += 1
    if is_disappointed(order, c):
        disappointed_count += 1

# 確率を計算
print(1 - disappointed_count / total)
