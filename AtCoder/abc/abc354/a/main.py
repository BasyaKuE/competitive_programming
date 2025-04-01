import bisect
import itertools
import sys
import collections

H = int(input())
now = 0
for i in range(100):
    now += 2**i
    if now > H:
        print(i+1)
        exit()
