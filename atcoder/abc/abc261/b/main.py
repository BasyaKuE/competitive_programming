import bisect
import itertools
import sys
import collections

N = int(input())
A = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and A[i][j] == A[j][i]:
            if A[i][j] == "D" and A[j][i] == "D":
                continue
            else:
                print("incorrect")
                exit()
        elif i != j and (A[i][j] == "D" or A[j][i] == "D"):
            print("incorrect")
            exit()
print("correct")
