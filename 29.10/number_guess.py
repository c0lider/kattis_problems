"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Guess the Number
Link: https://open.kattis.com/contests/eo92fp/problems/guess

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Binary Search

Status: Accepted 
Runtime: 0.04s
"""

number = 500
max_number = 1000
min_number = 1
counter = 0

while counter < 10:
    counter += 1
    print(number)
    feedback = input()

    if feedback == "correct":
        break
    elif feedback == "higher":
        min_number = number + 1
    elif feedback == "lower":
        max_number = number - 1

    number = (min_number + max_number) // 2
