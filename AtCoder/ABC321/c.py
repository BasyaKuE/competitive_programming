import heapq

K = int(input())
h = list(range(1,10))
heapq.heapify(h)

for i in range(K):
    n = heapq.heappop(h)
    for j in range(n % 10):
        heapq.heappush(h, n*10 + j)

print(n)
