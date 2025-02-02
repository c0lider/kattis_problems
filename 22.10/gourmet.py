"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: The Gourmet
Link: https://open.kattis.com/contests/v499w5/problems/gourmeten

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Dynamic Programming

Status: Accepted 
Runtime: 0.04s
"""

minutes = int(input())
courses = int(input())

dishes = []
for _ in range(courses):
    dishes.append(int(input()))

results = [0] * (minutes + 1)
results[0] = 1

for time in range(1, minutes + 1):
    for dish in dishes:
        if time - dish >= 0:
            results[time] += results[time - dish]

print(results[minutes])
