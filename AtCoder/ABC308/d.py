from collections import deque

def can_move_to_destination(grid, H, W):
    # 移動パターンを定義する
    pattern = "snuke"
    pattern_index = 0

    # BFS（幅優先探索）を使用して問題を解く
    queue = deque([(1, 1)])  # スタート地点
    visited = set()  # すでに訪れたセルを記録

    while queue:
        i, j = queue.popleft()

        # すでに訪れたセルの場合は無視
        if (i, j) in visited:
            continue

        visited.add((i, j))

        # 文字がパターンと一致しない場合、探索を中止
        if grid[i-1][j-1] != pattern[pattern_index]:
            continue

        # 終点に到達した場合、探索を終了
        if (i, j) == (H, W):
            return "Yes"

        # パターンの次の文字に移動
        pattern_index = (pattern_index + 1) % len(pattern)

        # 上下左右に移動できる場合は、そのセルをキューに追加
        if i > 1: queue.append((i-1, j))  # 上
        if i < H: queue.append((i+1, j))  # 下
        if j > 1: queue.append((i, j-1))  # 左
        if j < W: queue.append((i, j+1))  # 右

    # 終点に到達できなかった場合は "No"
    return "No"

# 入力からグリッドを作成
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# 関数を呼び出して結果を出力
print(can_move_to_destination(grid, H, W))
