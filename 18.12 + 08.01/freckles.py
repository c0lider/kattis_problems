"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Freckles
Link: https://open.kattis.com/contests/m68tjy/problems/freckles

@author Oliver Seiffermann
@version 3.0, 02/01/2024

Method: Minimum Spanning Tree

Status: Accepted
Runtime: 0.55s
"""

from typing import List, Tuple
from math import sqrt
from heapq import heappush, heappop


def get_euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_total_ink(coordinates: List[Tuple[float, float]]) -> float:
    if not coordinates:
        return 0.0

    num_coordinates = len(coordinates)
    if num_coordinates == 1:
        return 0.0

    visited = [False] * num_coordinates
    min_edge = [(float("inf"), -1)] * num_coordinates

    min_edge[0] = (0, 0)

    # (weight, node)
    priority_queue = [(0, 0)]
    total_distance = 0

    while priority_queue:
        weight, current_node = heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True
        total_distance += weight

        source_x, source_y = coordinates[current_node]
        for next_node in range(num_coordinates):
            if not visited[next_node]:
                target_x, target_y = coordinates[next_node]
                distance = get_euclidean_distance(
                    source_x, source_y, target_x, target_y
                )

                if distance < min_edge[next_node][0]:
                    min_edge[next_node] = (distance, current_node)
                    heappush(priority_queue, (distance, next_node))

    return total_distance


no_tests = int(input())

for i in range(no_tests):
    # skip blank line
    input()
    no_freckles = int(input())
    coordinates = [tuple(map(float, input().split())) for _ in range(no_freckles)]

    total_ink = calculate_total_ink(coordinates)
    print(f"{total_ink:.2f}")

    if i < (no_tests - 1):
        print()
