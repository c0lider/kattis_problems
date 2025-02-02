"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Torn To Pieces
Link: https://open.kattis.com/contests/m68tjy/problems/torn2pieces

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Breadth First Search

Status: Accepted
Runtime: 0.04s
"""

from collections import defaultdict, deque


no_pieces = int(input())

pieces = [input().split() for _ in range(no_pieces)]
starting_station, target_station = input().split()

adjacency_list = defaultdict(set)
all_stations = set()

for piece in pieces:
    source, *destinations = piece
    adjacency_list[source].update(destinations)
    for destination in destinations:
        adjacency_list[destination].add(source)

    all_stations.add(source)
    all_stations.update(destinations)

queue = deque([starting_station])
predecessors = {station: None for station in all_stations}
visited = set([starting_station])

while queue:
    current_station = queue.popleft()

    if current_station == target_station:

        route = []
        while current_station is not None:
            route.append(current_station)
            current_station = predecessors[current_station]

        route.reverse()
        print(" ".join(route))
        break

    for neighbor in adjacency_list[current_station]:
        if neighbor not in visited:
            visited.add(neighbor)
            predecessors[neighbor] = current_station
            queue.append(neighbor)

else:
    print("no route found")
