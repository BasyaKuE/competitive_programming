import bisect
import itertools
import sys
import collections

def main():
    N = int(input())
    strings = list(map(str, input().split()))

    strings.sort()

    def longest_common_prefix(s1, s2):
        min_len = min(len(s1), len(s2))
        lcp_length = 0
        for i in range(min_len):
            if s1[i] != s2[i]:
                break
            lcp_length += 1
        return lcp_length

    total = 0
    for i in range(N - 1):
        total += longest_common_prefix(strings[i], strings[i+1])

    print(total)

if __name__ == '__main__':
    main()
