"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Guard Evaders
Link: https://open.kattis.com/contests/p6fq6m/problems/guardevaders

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Backtracking

Status: Accepted
Runtime: 0.06s
"""

guards, player_amount = map(int, input().split(" "))

guard_formation = list(input())
amount_winners = 0
visited_states = set()


def find_passable_indices(guard_formation):
    passable_indices = []

    for guard_index in range(len(guard_formation) - 1):
        if (guard_formation[guard_index] != "R") and (
            guard_formation[guard_index + 1] != "L"
        ):
            passable_indices.append(guard_index)

    return passable_indices


def move_after_guard(guard_index: int, guard_formation: str, moves_until_now: int):
    if moves_until_now + 1 == player_amount:
        print(1)
        exit()

    guard_formation[guard_index] = "R"

    guard_formation[guard_index + 1] = "L"

    state = (tuple(guard_formation), moves_until_now + 1)

    if state in visited_states:
        return

    visited_states.add(state)

    for index in find_passable_indices(guard_formation):
        move_after_guard(index, guard_formation[:], moves_until_now + 1)


for index in find_passable_indices(guard_formation):
    move_after_guard(index, guard_formation[:], 0)

print(0)
