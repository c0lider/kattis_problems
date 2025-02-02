"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Hangman
Link: https://open.kattis.com/contests/v499w5/problems/hangman

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

word = input()
guesses = input()

word_set = set(word)
count = 0

for guess in guesses:
    try:
        word_set.remove(guess)
    except KeyError:
        count += 1
    if count > 9:
        print("LOSE")
        break
    if not word_set:
        print("WIN")
        break
