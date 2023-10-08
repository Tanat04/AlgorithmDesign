def dfs(row, col, h, w, tokens):
    if row < 0 or row >= h or col < 0 or col >= w or tokens[row][col] == -1:
        return 0

    current_token = tokens[row][col]
    tokens[row][col] = -1  # Mark the current square as visited

    below = dfs(row + 1, col, h, w, tokens)
    left = dfs(row + 1, col - 1, h, w, tokens)
    right = dfs(row + 1, col + 1, h, w, tokens)

    tokens[row][col] = current_token  # Restore the value of the current square

    return current_token + max(below, left, right)


def max_token_value(h, w, tokens):
    max_value = 0
    for col in range(w):
        max_value = max(max_value, dfs(0, col, h, w, tokens))

    return max_value


h1, w1 = 6, 5
tokens1 = [
    [6, 2, 5, 3, 1],
    [3, 1, 8, 4, 2],
    [2, 1, 3, 1, 1],
    [1, 2, 2, 1, 6],
    [2, 2, 1, 4, 3],
    [2, 1, 4, 5, 4]
]  # 5,8,1,6,4,5
# Calculate the maximum possible total token value
max_total_value = max_token_value(h1, w1, tokens1)
# Output the result
print(max_total_value)

# Sample input 2
h, w = 6, 6
tokens = [
    [5, 3, 2, 8, 7, 4],
    [4, 9, 6, 2, 1, 3],
    [7, 5, 8, 9, 4, 6],
    [3, 1, 2, 7, 9, 5],
    [2, 8, 3, 4, 6, 7],
    [9, 7, 1, 8, 5, 2]
]  # 8,6,9,9,6,8
# Calculate the maximum possible total token value
max_total_value = max_token_value(h, w, tokens)
# Output the result
print(max_total_value)
