# Understanding
# looping through array, alternating elements go to team1/team2
# returning a list of the sum of weights between team 1 and team 2 - ex: [180, 105]

# Planning
# results = []
# team1 = team2 = 0
# teamCounter = 1
# for weight in a:
    # if teamCounter % 2 != 0:
        # team1 += weight
        # teamCounter += 1
    # if teamCounter % 2 == 0:
        # team2 += weight
        # teamCounter += 1
# return results.append(team1, team2)

# Execute
def alternatingSums(a):
    results = []
    team1 = team2 = 0
    teamCounter = 1
    for weight in a:
        if teamCounter % 2 != 0:
            team1 += weight
            teamCounter += 1
        else:
            team2 += weight
            teamCounter += 1
    results = [team1, team2]
    return results

# Reflect/Refactor
def alternatingSums(a):
    return [sum(a[::2]),sum(a[1::2])]