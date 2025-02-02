"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Coast Length
Link: https://open.kattis.com/contests/m68tjy/problems/coast

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Floodfill + Coastline Calculation

Status: Accepted
Runtime: 0.86s
"""

from typing import List
from typing import Tuple

SEA = "0"
LAND = "1"
VISITED_SEA = "-"


def calculate_coast_length(grid: List[str]) -> int:
    mark_sea(grid)

    height = len(grid)
    width = len(grid[0])

    coast_length = 0

    for y in range(height):
        for x in range(width):
            if grid[y][x] == LAND:
                neighbors = get_neighbors(x, y, grid)
                coast_length += sum(
                    [
                        1 if neighbor_type == VISITED_SEA else 0
                        for _, _, neighbor_type in neighbors
                    ]
                )

    return coast_length


def mark_sea(grid: List[str]) -> List[str]:
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop()
        grid[y] = grid[y][:x] + VISITED_SEA + grid[y][x + 1 :]

        neighbors = get_neighbors(x, y, grid)
        for neighbor_x, neighbor_y, neighbor_type in neighbors:
            if neighbor_type == SEA:
                queue.append((neighbor_x, neighbor_y))


def get_neighbors(x: int, y: int, grid: List[str]) -> List[Tuple[int, int, str]]:
    neighbors = []
    height = len(grid)
    width = len(grid[0])

    neighbor_coordinates_list = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

    for neighbor_x, neighbor_y in neighbor_coordinates_list:
        if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
            neighbor = (neighbor_x, neighbor_y, grid[neighbor_y][neighbor_x])
            neighbors.append(neighbor)

    return neighbors


def get_grid(width: int, height: int) -> List[str]:
    outer_coast = "0" * (width + 2)
    grid = []
    grid.append(outer_coast)

    for _ in range(height):
        grid.append("0" + input() + "0")

    grid.append(outer_coast)

    return grid


height, width = map(int, input().split())

print(calculate_coast_length(get_grid(width, height)))
