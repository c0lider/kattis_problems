"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Heir's Dilemma
Link: https://open.kattis.com/contests/iju6a9/problems/heirsdilemma

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Recursion

Status: Not Accepted - Time Limit Exceeded
Runtime: 0.38s
"""

start, finish = map(int, input().split(" "))

counter = 0

while start < finish:
    digits = list(map(int, set(str(start))))
    if len(set(digits)) < 6 or any(digit == 0 for digit in digits):
        start += 1
        continue

    for digit in digits:
        if start % digit != 0:
            break
    else:
        counter += 1

    start += 1

print(counter)
