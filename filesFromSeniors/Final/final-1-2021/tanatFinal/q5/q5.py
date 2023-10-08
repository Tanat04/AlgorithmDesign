# Read the number of rows and columns in the image
rows, cols = map(int, input().split())

# Initialize an empty 2D list to store the image data
image = []

# Read the image data into a 2D list
for i in range(rows):
    image.append(list(map(int, input().split())))

# Define a function to check if a pixel is a valid cloud pixel


def is_valid(i, j):
    # Check if the pixel at (i, j) is a valid cloud pixel
    return 0 <= i < rows and 0 <= j < cols and image[i][j] == 1

# Define a DFS function to explore connected cloud pixels and count their size


def dfs(i, j):
    if not is_valid(i, j):
        return 0

    # Mark the current pixel as visited by setting it to -1
    image[i][j] = -1

    size = 1

    # Explore neighboring pixels in all four directions
    size += dfs(i - 1, j)  # Up
    size += dfs(i + 1, j)  # Down
    size += dfs(i, j - 1)  # Left
    size += dfs(i, j + 1)  # Right

    return size


# Initialize the variable to store the size of the largest cloud
largest_cloud_size = 0

# Iterate through all pixels to find the largest cloud
for i in range(rows):
    for j in range(cols):
        if is_valid(i, j):
            cloud_size = dfs(i, j)
            largest_cloud_size = max(largest_cloud_size, cloud_size)

# Print the size of the largest cloud
print(largest_cloud_size)

# from disjointsets3 import *

# M, N = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(M)]

# def largest_cloud(matrix):
#     rows, cols = M, N
#     ds = DisjointSets(rows * cols)

#     # For every cloud pixel, try to union it with its adjacent cloud pixels
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 1:
#                 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # up, down, left, right (adj)
#                     if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1: # valid
#                         ds.union(i * cols + j, x * cols + y) # union the cloud pixels by their

#     # Find the size of the largest cloud
#     cloudcount = [0] * (rows * cols)
#     for i in range(rows*cols):
#         cloudcount[ds.findset(i)] += 1

#     return max(cloudcount)

# print(largest_cloud(matrix))
