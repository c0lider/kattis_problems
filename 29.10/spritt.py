"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Spritt
Link: https://open.kattis.com/contests/eo92fp/problems/spritt

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.31s
"""

no_classes, bottles_available = map(int, input().split(" "))
bottles_needed = 0

for _ in range(no_classes):
    bottles_needed += int(input())

if bottles_available >= bottles_needed:
    print("Jebb")
else:
    print("Neibb")
