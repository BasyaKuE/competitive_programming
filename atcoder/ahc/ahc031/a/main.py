import bisect
import itertools
import sys
from typing import List
import numpy as np

W, D, N = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(D)]

current_x, current_y = 0, 0

for day in range(D):
    for i, area in enumerate(requests[day]):
        side_length = int(area ** 0.5)
        while side_length * side_length < area:
            side_length += 1

        bottom_right_x = current_x + side_length
        bottom_right_y = current_y + side_length

        print(f"{current_x} {current_y} {bottom_right_x} {bottom_right_y}")

        current_x += side_length
        if current_x >= W:
            current_x = 0
            current_y += side_length

    current_x, current_y = 0, 0

x + y = 100
y = x - 40

2y = 60
y = 30
x = 70
