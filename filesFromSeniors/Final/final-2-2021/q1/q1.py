import heapq

# Read input
packets = list(map(int, input().split()))

# Create a min-heap (priority queue) from the packet lengths
heapq.heapify(packets)

# Initialize the total cost
total_cost = 0

# Combine packets until only one packet remains in the heap
while len(packets) > 1:
    # Extract the two smallest packets from the heap
    packet1 = heapq.heappop(packets)
    packet2 = heapq.heappop(packets)

    # Calculate the cost of combining the two packets
    combined_cost = packet1 + packet2

    # Add the combined packet back to the heap
    heapq.heappush(packets, combined_cost)

    # Add the combined cost to the total cost
    total_cost += combined_cost

# Print the minimum possible total cost
print(total_cost)

# packets = list(map(int, input().split()))

# cost = 0
# while len(packets) > 1:
#     a = min(packets)
#     packets.remove(a)
#     b = min(packets)
#     packets.remove(b)
#     cost += a + b
#     packets.append(a + b)

# print(cost)
