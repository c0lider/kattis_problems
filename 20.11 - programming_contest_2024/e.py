"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Airfare Agents
Link: https://open.kattis.com/contests/p6fq6m/problems/airfaregrants

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""

amount = int(input())

numbers = [int(input()) for _ in range(amount)]

min_price = min(numbers)
max_price = max(numbers)

result = int(min_price - (max_price / 2))

if result < 0:
    print(0)
else:
    print(result)
