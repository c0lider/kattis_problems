"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Palindromic Word Search?
Link: https://open.kattis.com/contests/p6fq6m/problems/palindromicwordsearch

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Dynamic Programming

Status: Not Accepted - Memory Limit Exceeded
Runtime: 3.46s
"""


def is_palindrome(s):
    return s == s[::-1]


def find_palindromes(word):
    no_words = len(word)
    dp = [[False] * no_words for _ in range(no_words)]

    palindromes = []

    for length in range(1, no_words + 1):
        for start in range(no_words - length + 1):
            end = start + length - 1
            if length == 1:
                dp[start][end] = True
            elif length == 2:
                dp[start][end] = word[start] == word[end]
            else:
                dp[start][end] = dp[start + 1][end - 1] and (word[start] == word[end])

            if dp[start][end]:
                palindromes.append((start, end))

    return palindromes


def largest_palindromic_rectangle(words):
    rows = len(words)
    cols = len(words[0])

    row_palindromes = [find_palindromes(row) for row in words]

    columns = ["".join(row[col] for row in words) for col in range(cols)]
    col_palindromes = [find_palindromes(col) for col in columns]

    max_area = 0

    for row_no, row_palindrome_list in enumerate(row_palindromes):
        for row_start, row_end in row_palindrome_list:
            row_width = row_end - row_start + 1

            if row_width * rows <= max_area:
                continue

            for col_no in range(row_start, row_end + 1):
                for col_start, col_end in col_palindromes[col_no]:
                    col_height = col_end - col_start + 1

                    if col_start <= row_no <= col_end:
                        curr_area = row_width * col_height
                        max_area = max(max_area, curr_area)

    return max_area


amount_words, len_words = map(int, input().split())
words = [input() for _ in range(amount_words)]

print(largest_palindromic_rectangle(words))
