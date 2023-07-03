N = int(input())
d = {}
for i in range(N):
    A, B = map(int, input().split())
    d[i+1] = (A*(10**20)/(A+B))
# print(d)
sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
# print(sorted_items)
ans = [item[0] for item in sorted_items]
print(*ans)
