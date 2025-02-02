"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Last Factorial Digit
Link: https://open.kattis.com/contests/acee7h/problems/lastfactorialdigit

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

amount_cases = int(input())
numbers = []

for _ in range(amount_cases):
    numbers.append(int(input()))

for number in numbers:
    current_last = 1
    for factor in range(1, number + 1):
        current_last = (current_last * factor) % 10

    print(current_last)
