import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # 各ノードまでの距離を無限大に初期化
    distances[start] = 0  # 開始ノードまでの距離は0
    queue = [(0, start)]  # (距離, ノード)のタプルを格納する優先度キュー

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # 距離が最小のノードを取り出す

        # もし取り出したノードまでの距離が現在の距離よりも大きい場合、スキップ
        if current_distance > distances[current_node]:
            continue

        # 隣接ノードの距離を更新する
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # もし隣接ノードまでの距離が現在の距離よりも小さい場合、更新する
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


N1, N2, M = map(int, input().split())
g = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
start_node = '1'  # スタートノードを指定

distances = dijkstra(g, start_node)

# 各ノードまでの最短距離を出力
for node, distance in distances.items():
    print(f"ノード {node} までの最短距離: {distance}")
