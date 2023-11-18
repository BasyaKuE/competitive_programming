# 入力を受け取る
N, M = map(int, input().split())
S = input()
T = input()

# 生成する必要のある文字列X
X = ['#'] * N

# 文字列SをTで置き換えることができるかどうかを調べる関数
def can_transform(X, S, T):
    # 角のケース: M == Nの場合
    if M == N:
        return T == S

    # 部分文字列Tは、文字列S内でM文字分の同じ部分文字列を見つけたときにのみ適用できる
    for i in range(N - M + 1):
        if S[i:i + M] == T:
            X[i:i + M] = T
            if ''.join(X) == S:
                return True
            else:
                # Tで置換した後にSが完成しなければ、Xをリセットする
                X[i:i + M] = ['#'] * M
    # すべての可能性を試してもSを作れなければFalse
    return False

# 判定結果を出力する
print("Yes" if can_transform(X, S, T) else "No")