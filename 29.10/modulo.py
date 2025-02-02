"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Modulo
Link: https://open.kattis.com/contests/eo92fp/problems/modulo

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

print(len(set([number % 42 for number in [int(input()) for _ in range(10)]])))
