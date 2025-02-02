"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: T9 Spelling
Link: https://open.kattis.com/contests/v499w5/problems/t9spelling

@author Oliver Seiffermann
@version 4.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.10s
"""

t9_mapping = {
    " ": "0",
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
}

case_amount = int(input())
output = ""

for index in range(case_amount):
    last_output = "-"
    current_output = ""
    line = input()
    output += f"Case #{index + 1}: "
    for letter in line:
        current_output = t9_mapping.get(letter, "")

        if current_output[0] == last_output[0]:
            output += " "

        output += current_output

        last_output = current_output

    output += "\n"

print(output)
