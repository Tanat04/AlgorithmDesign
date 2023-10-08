# Read input
num_rows, num_cols = map(int, input().split())
token_values = []
for _ in range(num_rows):
    row_values = list(map(int, input().split()))
    token_values.append(row_values)

# Initialize a 2D table to store the maximum total token values
dp_table = [[0] * num_cols for _ in range(num_rows)]

# Initialize the first row of the dp table with the token values from the board
dp_table[0] = token_values[0]

# Iterate through each row from the second row to the last
for i in range(1, num_rows):
    for j in range(num_cols):
        # Calculate the maximum token value by considering three possible moves
        max_value = dp_table[i - 1][j]  # Move directly below
        if j > 0:
            # Move diagonally left
            max_value = max(max_value, dp_table[i - 1][j - 1])
        if j < num_cols - 1:
            # Move diagonally right
            max_value = max(max_value, dp_table[i - 1][j + 1])

        # Add the current token value to the maximum value
        dp_table[i][j] = max_value + token_values[i][j]

# The maximum total token value is the maximum value in the last row of the dp table
max_total_token_value = max(dp_table[num_rows - 1])

# Print the result
print(max_total_token_value)
