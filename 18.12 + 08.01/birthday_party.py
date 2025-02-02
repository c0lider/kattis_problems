"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Birthday Party
Link: https://open.kattis.com/contests/m68tjy/problems/birthday

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Tarjan's Algorithm

Status: Accepted
Runtime: 0.10s
"""

from collections import defaultdict


def find_bridges(graph, node_count):
    # use tarjans algorithm + track discovery times
    def dfs(source_node, parent, visited, discovery_times, low_links, time, is_bridge):
        visited[source_node] = True
        discovery_times[source_node] = low_links[source_node] = time[0]
        time[0] += 1

        for target_node in graph[source_node]:
            if not visited[target_node]:
                dfs(
                    target_node,
                    source_node,
                    visited,
                    discovery_times,
                    low_links,
                    time,
                    is_bridge,
                )
                low_links[source_node] = min(
                    low_links[source_node], low_links[target_node]
                )

                # an edge (u,v) is a bridge, if the low-link value of v is greater than the
                # discovery time of u
                if low_links[target_node] > discovery_times[source_node]:
                    is_bridge[0] = True
            elif target_node != parent:
                low_links[source_node] = min(
                    low_links[source_node], discovery_times[target_node]
                )

    visited = [False] * node_count
    discovery_times = [-1] * node_count
    low_link_values = [-1] * node_count
    # use list to simulate global counter, since lists are passed by reference
    time = [0]
    is_bridge = [False]

    for node in range(node_count):
        if not visited[node]:
            # parent is -1 becaus each time this call is performed, a node is part of
            # a new strongly connected component (scc) and thus has no parent
            dfs(node, -1, visited, discovery_times, low_link_values, time, is_bridge)

    return is_bridge[0]


def solve(node_count, edges):
    graph = defaultdict(list)
    for source_node, target_node in edges:
        graph[source_node].append(target_node)
        graph[target_node].append(source_node)

    if find_bridges(graph, node_count):
        return "Yes"
    else:
        return "No"


for _ in range(10):
    line = input().strip()
    amount_people, connection_amount = map(int, line.split())
    if amount_people == 0 and connection_amount == 0:
        break

    connections = []
    for _ in range(connection_amount):
        first_friend, second_friend = map(int, input().strip().split())
        connections.append((first_friend, second_friend))

    print(solve(amount_people, connections))
