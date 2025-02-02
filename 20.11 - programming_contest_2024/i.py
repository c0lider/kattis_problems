"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Leapfrog Encryption
Link: https://open.kattis.com/contests/p6fq6m/problems/leapfrogencryption

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Finished
Runtime: -
"""


def encrypt(input_string, keys):
    # step 1
    result = ""
    for letter in input_string.lower():
        if letter.isalpha():
            result += letter

    # step 2
    numbers = []

    for key in keys:
        numbers.append(ord(key) - ord("a") + 2)

    # step 3
    result = [""] * len(input_string)
    remaining_letters = input_string[:]

    loop_counter = 0
    while remaining_letters:
        if loop_counter % 2 == 0:
            add_left_to_right(numbers[loop_counter])
        else:
            add_right_to_left(numbers[loop_counter])
        loop_counter += 1

    def add_left_to_right(step):
        empty_letters = 0
        for index in range(0, len(input_string)):
            if result[index] == "":
                empty_letters += 1
            if empty_letters % step == 0:
                result[index] = remaining_letters[0]
                remaining_letters = remaining_letters[1:]

    # step 4
    def add_right_to_left(step):
        empty_letters = 0
        for index in range(len(result), 0, -1):
            if result[index] == "":
                empty_letters += 1
            if empty_letters % step == 0:
                result[index] = remaining_letters[0]
                remaining_letters = remaining_letters[1:]


def decrypt():
    pass


mode, key = input().split(" ")
input_string = input()

if mode == "E":
    print(encrypt(input_string))
