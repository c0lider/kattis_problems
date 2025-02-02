"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Divvying Up
Link: https://open.kattis.com/contests/eo92fp/problems/divvyingup

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

input()

print("yes" if (sum(map(int, input().split(" "))) % 3 == 0) else "no")
