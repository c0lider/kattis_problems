"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Midi
Link: https://open.kattis.com/contests/eo92fp/problems/midi

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.94s
"""

amount = int(input())
messages = []

for _ in range(amount):
    partial_message = input()
    messages.append(partial_message[::-1])

message = "".join(reversed(messages))
print(message)
