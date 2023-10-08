from simplePriorityQueue import *
N = int(input())
House = []
for _ in range(N):
    House.append(list(map(int, input().split())))


# Selection_List = []
# for i in range(2*N-1):
#     # print all positive number or zero number that add up to h
#     sel = []
#     for j in range(N):
#         if i-j >= 0 and i-j < N:
#             sel.append((i, House[j][i-j]))
#     Selection_List.append(sel)

class state:
    def __init__(self, i, j, g):
        self.i = i
        self.j = j
        self.g = g
        self.index = None


PQ = Simple_Priority_Queue(lambda x, y: x.g > y.g)
s = state(-1, -1, 0)
PQ.enqueue(s)
p = []
for i in range(N):
    u = PQ.dequeue()
    p.append(u)

    for v in House[i]:
        a = state(-1, -1, v)
        PQ.enqueue(a)

u = PQ.dequeue()
p.append(u)

print(sum(list(map(lambda a: a.g, p))))

# # Input: Number of floors on the cruise ship (n)
# n = int(input())

# # List to store the values of things on each floor
# floor_values = []

# # Read the values of things on each floor
# for i in range(n):
#     values_on_floor = list(map(int, input().split()))
#     floor_values.append(values_on_floor)

# # Create a copy of the floor_values list for manipulation
# master_floor_values = floor_values.copy()

# # Initialize the total value that Lupin can take
# total_value = 0

# # Function to find the maximum value in each floor


# def find_max_value_in_floor(floor):
#     max_values = []
#     for items in floor:
#         max_values.append(max(items))
#     return max_values

# # Function to find the index of the maximum value in a list


# def find_index_of_max_value(lst, value):
#     max_indices = []
#     for i in range(len(lst)):
#         if lst[i] == value:
#             max_indices.append(i)
#     return max(max_indices)


# # Iterate through the floors from top to bottom
# for i in range(n - 1, -1, -1):
#     # Find the maximum value on each floor
#     max_values_on_floor = find_max_value_in_floor(master_floor_values)

#     # Find the index of the floor with the highest maximum value
#     max_value_index = find_index_of_max_value(
#         max_values_on_floor, max(max_values_on_floor))

#     # Add the maximum value from the floor to Lupin's total value
#     total_value += max_values_on_floor[max_value_index]

#     # Remove the maximum value from the floor's list of values
#     master_floor_values[max_value_index].remove(max(max_values_on_floor))

#     # Remove the floor from consideration
#     master_floor_values.pop(i)

# # Print the maximum total value that Lupin can take
# print(total_value)
