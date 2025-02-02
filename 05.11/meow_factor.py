"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Meow Factor
Link: https://open.kattis.com/contests/acee7h/problems/meowfactor

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

number = int(input())

highest_factor = 1

for factor in range(2, number):
    if factor**9 > number:
        break
    if number % factor**9 == 0:
        highest_factor = factor

print(highest_factor)
