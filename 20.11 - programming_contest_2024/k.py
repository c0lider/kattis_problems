"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Oooh I see
Link: https://open.kattis.com/contests/p6fq6m/problems/ooohisee

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""

no_rows, row_len = map(int, input().split(" "))

treasure_map = []
for _ in range(no_rows):
    treasure_map.append(input())

treasures = []

for row_index in range(1, no_rows - 1):
    for col_index in range(1, row_len - 1):
        if treasure_map[row_index][col_index] == "0":
            if (
                treasure_map[row_index - 1][col_index - 1] == "O"
                and treasure_map[row_index][col_index - 1] == "O"
                and treasure_map[row_index + 1][col_index - 1] == "O"
                and treasure_map[row_index - 1][col_index] == "O"
                and treasure_map[row_index + 1][col_index] == "O"
                and treasure_map[row_index - 1][col_index + 1] == "O"
                and treasure_map[row_index][col_index + 1] == "O"
                and treasure_map[row_index + 1][col_index + 1] == "O"
            ):
                treasures.append((row_index + 1, col_index + 1))

if len(treasures) > 1:
    print(f"Oh no! {len(treasures)} locations")
elif len(treasures) == 1:
    print(f"{treasures[0][0]} {treasures[0][1]}")
else:
    print("Oh no!")
