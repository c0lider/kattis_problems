"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Postal Delivery
Link: https://open.kattis.com/contests/eo92fp/problems/delivery

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted - Time Limit Exceeded
Runtime: >1.0s
"""

# TODO: Time Limit Exceeded


def calc_delivery_dist(deliveries: dict, total_capacity: int):
    total_distance = 0

    def deliver():
        letters_delivered = 0
        remaining_capacity = total_capacity

        location, letters_to_deliver = list(deliveries.items())[-1]
        distance = 2 * abs(location)

        while letters_delivered < total_capacity:
            if letters_to_deliver > remaining_capacity:
                deliveries[location] -= remaining_capacity
                break
            else:  # letters_to_deliver <= capacity
                letters_delivered += letters_to_deliver
                remaining_capacity -= letters_to_deliver
                deliveries.popitem()

            try:
                location, letters_to_deliver = list(deliveries.items())[-1]
            except:
                break

        return distance

    while deliveries:
        total_distance += deliver()

    return total_distance


no_addresses, capacity = map(int, input().split(" "))
deliveries = {}

for _ in range(no_addresses):
    location, letters = map(int, input().split(" "))
    deliveries[location] = letters
# no_addresses, capacity = 3, 100
# deliveries = {-10: 50, 10: 175, 25: 20}

# no_addresses, capacity = 5, 3
# deliveries = {-1002: 800,
#     -1001: 800,
#     -1000: 800,
#     -999: 800,
#     -998: 800
# }


sorted_deliveries = {location: deliveries[location] for location in sorted(deliveries)}
positive_deliveries = {
    location: deliveries[location] for location in deliveries if location > 0
}
negative_deliveries = {
    location: deliveries[location] for location in deliveries if location < 0
}

print(
    calc_delivery_dist(positive_deliveries, capacity)
    + calc_delivery_dist(negative_deliveries, capacity)
)
