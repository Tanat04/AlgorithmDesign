# Read the list of Chitauri soldiers on each consecutive aircraft
aircraft_soldiers = list(map(int, input().split()))


def minimum_damage(soldiers_list):

    # Base case: If there are 3 or fewer aircraft, no damage is taken
    if len(soldiers_list) <= 3:
        return 0
    else:
        temp_sum = []
        temp_dam = []

        # Calculate the damage for different shooting scenarios
        for i in range(len(soldiers_list)):
            remaining_soldiers = []

            if i == len(soldiers_list) - 2:
                remaining_soldiers = soldiers_list[1:i]
            elif i == len(soldiers_list) - 1:
                remaining_soldiers = soldiers_list[2:i]
            else:
                remaining_soldiers = soldiers_list[:i] + soldiers_list[i + 3:]

            temp_sum.append(sum(remaining_soldiers))
            temp_dam.append(remaining_soldiers)

        # Find the minimum damage scenario
        min_damage = min(temp_sum)
        min_damage_index = temp_sum.index(min_damage)
        remaining_soldiers_damage = temp_dam[min_damage_index]

        return min_damage + minimum_damage(remaining_soldiers_damage)


# Calculate and print the minimum damage
print(minimum_damage(aircraft_soldiers))


'''
aircraft_soldiers = list(map(int, input().split())): This line reads a list of integers from the user, representing the number 
of Chitauri soldiers on each consecutive aircraft. The input is split into a list called aircraft_soldiers.

def minimum_damage(soldiers_list):: This line defines a function minimum_damage that takes a list soldiers_list as its 
input parameter. This function will be used to calculate the minimum damage.

if len(soldiers_list) <= 3:: This is the base case of the recursive function. It checks if there are 3 or fewer aircraft 
in the list. If there are, it returns 0 because Ironman doesn't take any damage when there are only a few aircraft left to destroy.

Inside the else block, the code calculates the damage for different shooting scenarios:

temp_sum is an empty list to store the sums of remaining soldiers after each shooting scenario.
temp_dam is an empty list to store the remaining soldiers in each shooting scenario.
for i in range(len(soldiers_list)):: This loop iterates through each aircraft in the list, considering it as the 
starting point for the shooting scenario.

Depending on the position of the current aircraft (i), it calculates the remaining soldiers after destroying three
adjacent aircraft. This is done using the remaining_soldiers list.

temp_sum.append(sum(remaining_soldiers)): It calculates the sum of remaining soldiers in the current shooting 
scenario and appends it to the temp_sum list.

temp_dam.append(remaining_soldiers): It appends the remaining_soldiers list to the temp_dam list.

After the loop, the code finds the minimum damage scenario:

min_damage stores the minimum sum of remaining soldiers from the temp_sum list.
min_damage_index stores the index of the minimum damage scenario in the temp_sum list.
remaining_soldiers_damage stores the corresponding remaining soldiers for the minimum damage scenario 
from the temp_dam list.
Finally, the function returns the sum of the minimum damage (min_damage) and the result of a recursive 
call to minimum_damage with the remaining_soldiers_damage as the argument. This recursion continues until the base case is reached.

print(minimum_damage(aircraft_soldiers)): It calls the minimum_damage function with the aircraft_soldiers 
list as an argument and prints the minimum damage Ironman will take.'''
