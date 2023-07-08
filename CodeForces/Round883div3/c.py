t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    scores = []
    for i in range(n):
        times = sorted(list(map(int, input().split())))
        time = 0
        solve = 0
        for j in range(m):
            if time+times[j] > h:
                continue
            else:
                time += times[j]
                solve += 1
        scores.append([solve, time, i])

    scores.sort(key=lambda x: (-x[0], x[1]))
    print(scores)
    for i, sublist in enumerate(scores):
        if sublist[2] == 0:
            print(i + 1)  # 1-indexedとして表示
            break  # 最初に見つかったものだけ出力
