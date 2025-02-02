"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Exam
Link: https://open.kattis.com/contests/uaitfj/problems/exam

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""


def count_matching_positions(str1, str2):
    # assuming both strings are of equal length
    return sum(1 for i in range(len(str1)) if str1[i] == str2[i])


amount_correct = int(input())
my_answers = input()
friends_answers = input()

matching_answers = count_matching_positions(my_answers, friends_answers)
amount_not_matching = len(friends_answers) - matching_answers

if matching_answers >= amount_correct:
    max_correct = amount_correct + amount_not_matching
else:
    max_correct = (
        matching_answers + amount_not_matching - (amount_correct - matching_answers)
    )

print(max_correct)
