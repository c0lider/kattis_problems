"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Longes Increasing Subsequence
Link: https://open.kattis.com/contests/rfq9ju/problems/longincsubseq

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Dynamic Programming

Status: Accepted
Runtime: 0.18s
"""

import sys
from bisect import bisect_left


def get_longest_increasing_subsequence(sequence):
    sequence_length = len(sequence)
    if sequence_length == 0:
        return 0, []

    tails = []
    prev = [-1] * sequence_length
    indices = [-1] * sequence_length

    for i, num in enumerate(sequence):
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
        indices[pos] = i
        if pos > 0:
            prev[i] = indices[pos - 1]

    lis_length = len(tails)
    last_index = indices[lis_length - 1]
    lis_indices = []
    while last_index != -1:
        lis_indices.append(last_index)
        last_index = prev[last_index]

    lis_indices.reverse()
    return lis_length, list(map(str, lis_indices))


for line in sys.stdin:
    numbers = list(map(int, input().split()))
    length, indices = get_longest_increasing_subsequence(numbers)

    print(length)
    print(" ".join(indices))
