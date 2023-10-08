def can_complete_circuit(Petrol, Distance):
    surplus, deficit, start = 0, 0, 0

    for i in range(len(Petrol)):
        surplus += Petrol[i] - Distance[i]

        if surplus < 0:
            deficit += surplus
            surplus = 0
            start = i + 1

    return start if surplus + deficit >= 0 else -1


# Input
N = int(input())
Petrol = list(map(int, input().split()))
Distance = list(map(int, input().split()))

# Output
starting_station = can_complete_circuit(Petrol, Distance)
print(starting_station)
