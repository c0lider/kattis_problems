"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Natjecanje
Link: https://open.kattis.com/contests/iju6a9/problems/natjecanje

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""

no_total, no_damaged, no_reserve = map(int, input().split(" "))

teams_with_dmg = list(map(int, input().split(" ")))
teams_with_reserve = list(map(int, input().split(" ")))

self_providing_teams = list(set(teams_with_dmg) & set(teams_with_reserve))

for team in self_providing_teams:
    teams_with_dmg.remove(team)
    teams_with_reserve.remove(team)

teams_with_dmg.sort()
teams_with_reserve.sort()

teams_not_participating = 0

for team_with_dmg in teams_with_dmg:
    previous_team = team_with_dmg - 1
    next_team = team_with_dmg + 1

    if previous_team in teams_with_reserve:
        teams_with_reserve.remove(previous_team)
    elif next_team in teams_with_reserve:
        teams_with_reserve.remove(next_team)
    else:
        teams_not_participating += 1

print(teams_not_participating)
