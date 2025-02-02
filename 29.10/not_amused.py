"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Modulo
Link: https://open.kattis.com/contests/eo92fp/problems/notamused

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted 
Runtime: 0.06s
"""

# TODO: Does not work - Run-Time Error on submission

PRICE_PER_MINUTE = 0.1


def print_times(day_no: int, minutes_spent: dict):
    print(f"Day {day_no}")
    sorted_minutes_spent = {name: minutes_spent[name] for name in sorted(minutes_spent)}
    for name, minutes in sorted_minutes_spent.items():
        price = "{:,.2f}".format(minutes * PRICE_PER_MINUTE)
        print(f"{name} ${price}")
    print()


def calc_day(day_no: int):
    enter_times = {}
    minutes_spent = {}
    current_input = input()

    while current_input != "CLOSE":
        current_input = current_input.split(" ")

        if current_input[0] == "ENTER":
            name = current_input[1]
            enter_time = current_input[2]
            enter_times[name] = int(enter_time)
        elif current_input[0] == "EXIT":
            name = current_input[1]
            exit_time = int(current_input[2])
            minutes_spent[name] = (
                minutes_spent.get(name, 0) + exit_time - enter_times[name]
            )

        current_input = input()
    print_times(day_no, minutes_spent)


counter = 1

while 1:
    current_input = input()
    calc_day(counter)
    counter += 1
