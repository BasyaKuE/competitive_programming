import bisect
import itertools
import sys
import collections

N = int(input())
cards = []
for index in range(N):
    A, C = map(int, input().split())
    cards.append((A, C, index + 1))
cards.sort(key=lambda x: (x[1], -x[0]))
filtered_cards = []
max_a = -1
for A, C, index in cards:
    if A > max_a:
        filtered_cards.append(index)
        max_a = A
filtered_cards.sort()
print(len(filtered_cards))
print(*filtered_cards)
