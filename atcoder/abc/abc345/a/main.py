import bisect
import itertools
import sys
from typing import List

S = input()
for i in range(len(S)):
    if i == 0 and S[i] != "<":
        print("No")
        exit()
    if i == len(S)-1 and S[i] != ">":
        print("No")
        exit()
    elif i != 0 and i != len(S)-1 and S[i] != "=":
        print("No")
        exit()
print("Yes")
