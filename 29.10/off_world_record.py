"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Off World Records
Link: https://open.kattis.com/contests/eo92fp/problems/offworldrecords

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

amount_jumps, current_record, previous_record = map(int, input().split(" "))
new_records = 0

for _ in range(amount_jumps):
    current_jump = int(input())
    if current_jump > current_record + previous_record:
        new_records += 1
        previous_record = current_record
        current_record = current_jump

print(new_records)
