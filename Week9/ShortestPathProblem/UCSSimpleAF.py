from simplePriorityQueue import Simple_Priority_Queue

# Read the number of cities
V = int(input())
# Initialize an adjacency list for the cities
adj_list = [[] for _ in range(V)]

# Read information about edges (connections between cities) and their distances
while True:
    try:
        u, v, w = map(int, input().split())
        # Add the edge from city 'u' to city 'v' with distance 'w' to the adjacency list
        adj_list[u].append((v, w))
        # Since it's an undirected graph, add the reverse edge as well
        adj_list[v].append((u, w))
    except:
        # Stop reading input when an exception occurs (end of input)
        break

# Define a class to represent a state in the search


class state:
    def __init__(self, u, g):
        self.u = u  # Current city
        self.g = g  # Total cost from start to this state
        self.parent = None  # Reference to the parent state

    # Generate successor states (cities reachable from the current city)
    def successor(self):
        succ = []
        for v, w in adj_list[self.u]:
            # Create a new state for each neighbor
            x = state(v, self.g + w)
            x.parent = self  # Set the parent to the current state
            succ.append(x)
        return succ

    # Check if the current state is the goal state (reached the destination city)
    def is_goal(self):
        return self.u == V - 1

# Uniform Cost Search (UCS) function


def UFS(s):
    simplePQ = Simple_Priority_Queue(lambda x, y: x.g < y.g)
    simplePQ.enqueue(s)
    Explored = set()

    while not simplePQ.empty():
        node = simplePQ.dequeue()
        Explored.add(node)
        if node.is_goal():
            return node.g, node  # Return the total cost and the goal state

        for suc in node.successor():
            if suc not in Explored:
                simplePQ.enqueue(suc)

# Reconstruct and return the path from the start to the goal state


def getPath(s):
    path = []
    while s != None:
        # Insert the current city at the beginning of the path
        path.insert(0, s.u)
        s = s.parent  # Move to the parent state
    return path


# Initialize the start state (city 0 with a total cost of 0)
s = state(0, 0)
# Run the UCS search and store the result in 'cost' and 'goal'
cost, goal = UFS(s)
# Retrieve the path from the start to the goal state
path = getPath(goal)

# Print the total cost of the shortest route
print(cost)
# Print the cities visited along the path
for i in range(len(path) - 1):
    print(path[i], end='->')
print(path[-1])  # Print the last city in the path
