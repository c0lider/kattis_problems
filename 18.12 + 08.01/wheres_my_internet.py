"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Where's my Internet?
Link: https://open.kattis.com/contests/m68tjy/problems/wheresmyinternet

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Breadth First Search

Status: Accepted
Runtime: 0.36s
"""

from collections import defaultdict, deque
from typing import List, Tuple


def get_connected_nodes_bfs(
    root_node: int, connections: List[Tuple[int, int]]
) -> List[int]:
    adjacency_list = defaultdict(list)

    for source, target in connections:
        adjacency_list[source].append(target)
        adjacency_list[target].append(source)

    visited = set()
    queue = deque([root_node])
    visited.add(root_node)

    while queue:
        node = queue.popleft()
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return list(visited)


no_houses, cables_deployed = map(int, input().split())
cable_connections = [tuple(map(int, input().split())) for _ in range(cables_deployed)]

house_connected_to_root = get_connected_nodes_bfs(1, cable_connections)

all_houses = set(range(1, no_houses + 1))
houses_not_connected = all_houses.difference(house_connected_to_root)

if len(houses_not_connected) == 0:
    print("Connected")
else:
    for house in sorted(houses_not_connected):
        print(house)
