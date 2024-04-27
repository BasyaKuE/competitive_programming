import bisect
import itertools
import sys
import collections

N = int(input())
A = list(map(int, input().split()))
stack = []

for i in range(N):
    stack.append(A[i])
    # print(stack)
    if len(stack) <= 1:
        continue
    while stack[-1] == stack[-2]:
        a = stack.pop()
        b = stack.pop()
        stack.append(a+1)
        if len(stack) <= 1:
            break
print(len(stack))
