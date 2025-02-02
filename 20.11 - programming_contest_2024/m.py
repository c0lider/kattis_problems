"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Welcome Sign
Link: https://open.kattis.com/contests/p6fq6m/problems/welcomesign

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""

import math

rows, cols = map(int, input().split(" "))

words = []
odd_row_count = 0

for _ in range(rows):
    words.append(input())

for row_no, word in enumerate(words):
    total_padding = cols - len(word)
    right_padding = 0
    left_padding = 0

    if total_padding % 2 != 0:
        odd_row_count += 1

    if (odd_row_count) % 2 == 1:
        left_padding = math.floor(total_padding / 2)
        right_padding = math.ceil(total_padding / 2)
    else:
        left_padding = math.ceil(total_padding / 2)
        right_padding = math.floor(total_padding / 2)

    print("." * left_padding, word, "." * right_padding, sep="")
