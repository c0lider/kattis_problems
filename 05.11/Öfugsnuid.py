"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Ofugsnuid
Link: https://open.kattis.com/contests/acee7h/problems/ofugsnuid

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.13s
"""

amount = int(input())

numbers = [input() for _ in range(amount)]
numbers.reverse()

print("\n".join(numbers))
