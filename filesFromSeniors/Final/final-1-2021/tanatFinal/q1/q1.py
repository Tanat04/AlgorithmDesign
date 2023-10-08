from disjointsets3 import DisjointSets

# Input: Number of cities (n) and number of high-speed lines (m)
n, m = map(int, input().split())

# List to store information about potential high-speed lines
potential_lines = [tuple(map(int, input().split())) for _ in range(m)]


def find_minimum_cost_to_build_network(n, potential_lines):
    # Sort the potential lines by their costs in ascending order
    sorted_lines = sorted(potential_lines, key=lambda x: x[2])

    # Create a Disjoint Set data structure
    disjoint_sets = DisjointSets(n)

    total_cost = 0  # To store the minimum possible cost
    built_lines = 0  # To count the number of built lines

    for city1, city2, cost in sorted_lines:
        # Check if adding this line connects two cities without forming a cycle
        if disjoint_sets.findset(city1) != disjoint_sets.findset(city2):
            # Union the sets of city1 and city2
            disjoint_sets.union(city1, city2)
            total_cost += cost  # Add the cost of building this line to the total cost
            built_lines += 1

        # Check if we have built enough lines to connect all cities
        if built_lines == n - 1:
            break

    return total_cost


# Calculate and print the minimum possible cost to build all necessary high-speed lines
minimum_cost = find_minimum_cost_to_build_network(n, potential_lines)
print(minimum_cost)


# from disjointsets3 import DisjointSets
# V, E = map(int, input().split())
# Edges = [tuple(map(int, input().split())) for _ in range(E)]


# def Kruskal(V, Edges):
#     Edges = sorted(Edges, key=lambda x: x[2])

#     # Create Disjoint Set
#     D = DisjointSets(V)

#     W = 0
#     edgecount = 0

#     for u, v, w in Edges:
#         if D.findset(u) != D.findset(v):
#             D.union(u, v)
#             print(u, v, w)
#             W += w
#             edgecount += 1

#     print(W)


# Kruskal(V, Edges)
