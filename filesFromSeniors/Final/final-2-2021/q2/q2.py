def matrix_multiply(A, B):
    # Multiply two matrices A and B
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (A[i][k] * B[k][j]) % 2147483647
                result[i][j] %= 2147483647
    return result


def matrix_power(M, n):
    # Compute M^n using matrix exponentiation
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, M)
        M = matrix_multiply(M, M)
        n //= 2
    return result


def fibonacci_modulo(n):
    if n <= 1:
        return n

    # Initialize the base matrix
    base_matrix = [[1, 1], [1, 0]]

    # Compute the n-th power of the base matrix
    result_matrix = matrix_power(base_matrix, n)

    # The Fibonacci number F(n) is the top left element of the result matrix
    return result_matrix[0][0] % 2147483647


# Read input
n = int(input())

# Calculate and print F(n) modulo 2147483647
result = fibonacci_modulo(n)
print(result)

# MOD = 2147483647

# # Multiplies two matrices under modulo MOD
# def mat_mult(A, B):
#     """Multiply matrix A and B modulo MOD."""
#     n = len(A)
#     m = len(A[0])
#     p = len(B[0])

#     C = [[0] * p for _ in range(n)]
#     for i in range(n):
#         for j in range(p):
#             for k in range(m):
#                 C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
#     return C

# # Computes matrix power using exponentiation by squaring
# def mat_pow(m, n):
#     if n == 1:
#         return m


#     half_pow = mat_pow(m, n // 2)
#     if n % 2 == 0:
#         return mat_mult(half_pow, half_pow)
#     else:
#         return mat_mult(mat_mult(half_pow, half_pow), m)

# def fibonacci_modulo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = mat_pow([[1, 1], [1, 0]], n-1)
#         return (result[0][0] + result[0][1]) % MOD

# # Test the function
# print(fibonacci_modulo(123456789))             # Output: 2053005829
# print(fibonacci_modulo(12345678901234567890))  # Output: 268002575
