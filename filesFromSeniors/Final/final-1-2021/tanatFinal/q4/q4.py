# Read input values
N, T, R = map(int, input().split())
pages_saturday = list(map(int, input().split()))
pages_sunday = list(map(int, input().split()))

# Initialize the total extra payments
total_extra_payments = 0

# Sort the pages to be typed on Saturday in ascending order
pages_saturday.sort()

# Sort the pages to be typed on Sunday in descending order
pages_sunday.sort(reverse=True)

# Iterate through the documents
for i in range(N):
    total_pages = pages_saturday[i] + pages_sunday[i]
    if total_pages > T:
        extra_pages = total_pages - T
        extra_payment = extra_pages * R
        total_extra_payments += extra_payment

# Calculate the minimum possible extra payments
print(total_extra_payments)


# N, P, E = map(int, input().split())
# l = []
# for i in range(2):
#     l.append(list(map(int, input().split())))
# l[0].sort()
# l[1].sort(reverse=True)
# total = 0
# for i in range(N):
#     result = l[0][i] + l[1][i]
#     if result > P:
#         extra = (result - P) * E
#         total += extra
# print(total)
